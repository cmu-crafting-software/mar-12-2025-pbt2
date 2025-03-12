# Adapted from: https://rosettacode.org/wiki/Modular_inverse#Python
#
# The modular multiplicative inverse of an integer `a` modulo `m` is an
# integer 'x' such that:
#   `a x ≡ 1 ( mod m )`
# In other words, the remainder after dividing `ax` by the integer `m` is 1
#
# @param a finite integer > 0
# @param m finite integer > 0 (modulus)
# @returns a finite integer such that ax % m = 1
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m

def extended_gcd(a, b):
    lastremainder, remainder = abs(a), abs(b)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if a < 0 else 1), lasty * (-1 if b < 0 else 1)
