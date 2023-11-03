import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def generate_keys(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)

    if gcd(phi, e) != 1:
        raise ValueError("e is not coprime with phi(n). Choose a different value of e.")

    _, d, _ = extended_gcd(e, phi)
    d = d % phi
    if d < 0:
        d += phi

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def sign_message(message, private_key):
    d, n = private_key
    signature = pow(message, d, n)
    return signature

def generate_keys_and_sign_menu():
    p = int(input("Enter the value of prime number p: "))
    q = int(input("Enter the value of prime number q: "))
    e = int(input("Enter the public key value e: "))

    public_key, private_key = generate_keys(p, q, e)
    print("Public key (e, n):", public_key)
    print("Private key (d, n):", private_key)

    message = int(input("Enter the message to sign: "))
    signature = sign_message(message, private_key)
    print("Digital signature:", signature)

if __name__ == "__main__":
    generate_keys_and_sign_menu()
