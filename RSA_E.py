p=int(input("Enter p: "))
q=int(input("Enter q: "))
e=int(input("Enter e: "))
m=int(input("Enter msg: "))
n = p*q
phi = (p-1)*(q-1)

d = pow(e,-1,phi)
print(f"public key (e, n): ({e}, {n})")
print(f"private key (d,n): ({d}, {n})")

encrypted_text = pow(m,e,n)
print(f"encrypted text is is ", encrypted_text)