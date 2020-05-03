import itertools
import md5
import string
import hashlib

alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits

# does not end with a digit
# Na5Tmo
for g in itertools.product(alphabet, repeat=6):
		guess = "".join(g)
		if hashlib.md5(guess).hexdigest() == "ab59fb49bd66228831663de74eaa7628":
			print(guess)
			exit()
