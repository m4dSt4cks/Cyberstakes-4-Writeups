"""
The following Python implementation of Shamir's Secret Sharing is
released into the Public Domain under the terms of CC0 and OWFa:
https://creativecommons.org/publicdomain/zero/1.0/
http://www.openwebfoundation.org/legal/the-owf-1-0-agreements/owfa-1-0

See the bottom few lines for usage. Tested on Python 2 and 3.
"""

from __future__ import division
from __future__ import print_function

import random
import functools
import binascii

# 12th Mersenne Prime
# (for this application we want a known prime number as close as
# possible to our security level; e.g.  desired security level of 128
# bits -- too large and all the ciphertext is large; too small and
# security is compromised)
_PRIME = 2**521 - 1
# 13th Mersenne Prime is 2**521 - 1 GOOD THING THIS WAS HERE

_RINT = functools.partial(random.SystemRandom().randint, 0)

def _eval_at(poly, x, prime):
    """Evaluates polynomial (coefficient tuple) at x, used to generate a
    shamir pool in make_random_shares below.
    """
    accum = 0
    for coeff in reversed(poly):
        accum *= x
        accum += coeff
        accum %= prime
    return accum

def _extended_gcd(a, b):
    """
    Division in integers modulus p means finding the inverse of the
    denominator modulo p and then multiplying the numerator by this
    inverse (Note: inverse of A is B such that A*B % p == 1) this can
    be computed via extended Euclidean algorithm
    http://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Computation
    """
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while b != 0:
        quot = a // b
        a, b = b, a % b
        x, last_x = last_x - quot * x, x
        y, last_y = last_y - quot * y, y
    return last_x, last_y

def _divmod(num, den, p):
    """Compute num / den modulo prime p

    To explain what this means, the return value will be such that
    the following is true: den * _divmod(num, den, p) % p == num
    """
    inv, _ = _extended_gcd(den, p)
    return num * inv

def _lagrange_interpolate(x, x_s, y_s, p):
    """
    Find the y-value for the given x, given n (x, y) points;
    k points will define a polynomial of up to kth order.
    """
    k = len(x_s)
    assert k == len(set(x_s)), "points must be distinct"
    def PI(vals):  # upper-case PI -- product of inputs
        accum = 1
        for v in vals:
            accum *= v
        return accum
    nums = []  # avoid inexact division
    dens = []
    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        nums.append(PI(x - o for o in others))
        dens.append(PI(cur - o for o in others))
    den = PI(dens)
    num = sum([_divmod(nums[i] * den * y_s[i] % p, dens[i], p)
               for i in range(k)])
    return (_divmod(num, den, p) + p) % p

def recover_secret(shares, prime=_PRIME):
    """
    Recover the secret from share points
    (x, y points on the polynomial).
    """
    if len(shares) < 2:
        raise ValueError("need at least two shares")
    x_s, y_s = zip(*shares)
    return _lagrange_interpolate(0, x_s, y_s, prime)

def main():
    """Main function"""
    shares = []
    # shares.append((1, 9608474170977308238036624146101441469538628637045706610338073590812843162969037926492967854559828114435865261425719619743472419864336210874222029453059741))
    shares.append((2, 68500755079349789351078524541708453870296292990294021018027228505078681492284299873863659247273461856762128786874833326789786067325816477066780304059822843))
    shares.append((3, 224183841656780872927678242626279871433733831057475254917387185998520511272846647279913467443558309288829498488402883425874249712684215384203475752039681175))
    shares.append((4, 524164732834933988556388319839274528391312080836319720002737667326861328789556912063222725295339950383555529443266354316704089242529615243887408038702736241))
    shares.append((5, 1015950427545472565825761297620151258974491880324557727968398393745824130327315926142371765654543965113857776728721730398986530543452098367721676829359089545))

    print('Secret recovered from minimum subset of shares: ' + binascii.unhexlify(hex(recover_secret(shares)).lstrip("0x").rstrip("L")))

if __name__ == '__main__':
    main()
# https://en.wikipedia.org/wiki/Shamir's_Secret_Sharing

