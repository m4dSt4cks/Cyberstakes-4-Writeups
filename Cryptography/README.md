# Cryptography

## Rotate Me

[My favorite solver](https://www.dcode.fr/caesar-cipher)

## Really Senseless Admins

This involves calculating the private key from the public key in RSA. Hopefully the python script is self explanatory.

## Over Time: Paid

The generate_doc function creates several lines of randomness, but we know the first and last lines. The "OTP" that is generated is applied to every line. We can figure out the key by XORing the unencrypted intro with the first line of encrypted text. Then, we can used the key to decrypt the last line.

## Speak Plainly

This has to do with AES ECB encryption. In this mode, the same output is supplied every time the same input is provided. This means that we can encrypt our input and compare it to the output to look for a match. Other writeups have covered this attack in depth, so I'll just provide the python I used.

The solver finishes when '*' characters get printed out. Apologies for not really making it a malleable script.

## Headpiece Silver

To answer the hint's question, N is not that large. I used [this site](https://www.alpertron.com.ar/ECM.HTM) to factor it (Sage is much better). The solver after that is much like the first RSA problem.

## We're Related

I just stole an existing script for a similar problem. Since the RSA in this scheme doesn't use padding, we can create a related message by multiplying the flag by 2, decrypting it, and then dividing by 2.

## Pigeon Holes

I really enjoyed this problem. It has to do with zlib compression. Thankfully, if the firmware image is too large, it tells you exactly how many bytes it contains.

I first saw that the flag is part of the firmware that gets AES encrypted. Both the tag and nonce are thrown away after encryption, so we probably won't be able to decrypt it, at least not in the 10 days of the competition.

However, before encryption is applied, the data is compressed. Another thing we learn is how large the firmware image is *after* compression, which is important because our input directly influences this value.

Since we control the Vin number, we know that the string will look like Rev:2::Vin:INPUT::DeviceKey:FLAG.

If we were to guess the first letter of the flag correctly, we would get a slightly smaller number in the error message because more of the data is duplicated.

Finally, I ensured that my data would be too long to generate the firmware by prepending 1000 "{" characters. I also reduced some entropy by getting rid of the extra data by "reflashing" the code.

My script takes a while, so it may need to be run a couple times with the flag variable being updated when the server times out. 