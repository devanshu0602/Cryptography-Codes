import random # To randomly select value from set of possible values


def find_phi(num1, num2):
    return (num1 - 1) * (num2 - 1)


def gcd(num1, num2):
    if num1 == 0 or num1 == num2:
        return num2
    else:
        return gcd(num2 % num1, num1)


def find_e_values(phi_of_n):
    e_values = []
    for i in range(2, phi_of_n):
        if gcd(i, phi_of_n) == 1:
            e_values.append(i)
    return e_values


def find_d_value(e, phi_of_n):
    d = 1
    while (d * e) % phi_of_n != 1:
        d = d + 1
    return d


def encrypt(plain_text, e, n):
    plain_text = plain_text % n
    remainder = 1
    while e > 0:
        if e % 2 == 1:
            remainder = (remainder * plain_text) % n
        plain_text = (plain_text * plain_text) % n
        e = e // 2
    return remainder


def decrypt(cipher_text, d, n):
    cipher_text = cipher_text % n
    remainder = 1
    while d > 0:
        if d % 2 == 1:
            remainder = (remainder * cipher_text) % n
        cipher_text = (cipher_text * cipher_text) % n
        d = d // 2
    return remainder


# DRIVER FUNCTION
print("\n\n### RSA ALGORITHM ###\n\n")
# Prime numbers
print("Enter the 2 prime numbers:")
p = int(input("\t-> Number 1 (p) = "))
q = int(input("\t-> Number 2 (q) = "))
# Calculate n and Phi(n)
print("\nCalculating n and Phi(n) values:")
n = p * q
phi_of_n = find_phi(num1=p, num2=q)
print(f"\t-> n = (p * q) = ({p} * {q}) = {n}")
print(f"\t-> Phi(n) = Phi({n}) = {phi_of_n}")
# Computing e -> 1 < e < Phi(n) and GCD(e, Phi(n)) = 1
print("\nComputing 'e' s.t. 1 < e < Phi(n) & GCD(e, Phi(n)) = 1:")
e_values = find_e_values(phi_of_n)
e = random.choice(e_values)
print(f"\t-> Chosen value for e = {e}")
# Public key
print(f"\nTHE PUBLIC KEY = (e, n) = ({e}, {n})")
# Computing d -> d*e mod Phi(n) = 1
d = find_d_value(e, phi_of_n)
# Private key
print(f"\nTHE PRIVATE KEY = (d, n) = ({d}, {n})")
# Encryption
print("\n\nPerforming Encryption:")
plain_text = int(input("\t-> Enter the plain text = "))
cipher_text = encrypt(plain_text, e, n)
print(f"\nTHE ENCRYPTED TEXT IS = Encrypt({plain_text})")
print(f"\t= ({plain_text} ^ {e}) mod {n}")
print(f"\t= {cipher_text}")
# Decryption
print("\n\nPerforming Decryption:")
cipher_text = int(input("\t-> Enter the cipher text = "))
plain_text = decrypt(cipher_text, d, n)
print(f"\nTHE DECRYPTED TEXT IS = Decrypt({cipher_text})")
print(f"\t= ({cipher_text} ^ {d}) mod {n}")
print(f"\t= {plain_text}")
# Footer
print("\n\nDevanshu Gupta 21BCE0597\n\n")