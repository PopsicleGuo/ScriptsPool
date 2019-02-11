# try to iteration way for Greatest Common Divisor
def gcd(a,b):
    while b > 0:
        rem = a % b
        a = b
        b = rem
    return a

print(gcd(2,3))

# Recursion version
def gcd1(a, b):
    if b == 0:
        return b
    else:
        return gcd1(b, a%b)
print(gcd(2,3))