p=int(input("Enter p: "))
q=int(input("Enter q: "))
e=int(input("Enter e: "))
c=int(input("Enter encripted msg: "))
n = p*q
phi = (p-1)*(q-1)

d = pow(e,-1,phi)
print(f"public key (d,n): ({d}, {n})")
print(f"private key (e, n): ({e}, {n})")

decrypted_text = pow(c,d,n)
print(f"decrypted_text text is is ", decrypted_text)