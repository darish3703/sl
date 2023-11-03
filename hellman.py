def calculate_public_key(alpha, private_key, prime):
    return (alpha ** private_key) % prime

def calculate_shared_secret(public_key, private_key, prime):
    return (public_key ** private_key) % prime

def generate_keys(alpha, prime, xa, xb):
    public_key_a = calculate_public_key(alpha, xa, prime)
    public_key_b = calculate_public_key(alpha, xb, prime)
   
    shared_secret_a = calculate_shared_secret(public_key_b, xa, prime)
    shared_secret_b = calculate_shared_secret(public_key_a, xb, prime)
   
    return (public_key_a, public_key_b), (shared_secret_a, shared_secret_b)


q = int(input("Enter the prime number (q): "))
alpha = int(input("Enter the value of alpha (α): "))
xa = int(input("Enter the private key for Alice (XA): "))
xb = int(input("Enter the private key for Bob (XB): "))
   
keys, shared_secrets = generate_keys(alpha, q, xa, xb)
   
public_key_a, public_key_b = keys
shared_secret_a, shared_secret_b = shared_secrets
   
print("Public key of Alice (eA, n):", public_key_a, q)
print("Public key of Bob (eB, n):", public_key_b, q)
print("Shared secret of Alice:", shared_secret_a)
print("Shared secret of Bob:", shared_secret_b)
