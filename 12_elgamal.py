def find_mod(base, exponent, modulus):
    base = base % modulus
    remainder = 1
    while exponent > 0:
        if exponent % 2 == 1:
            remainder = (remainder * base) % modulus
        base = (base * base) % modulus
        exponent = exponent // 2
    return remainder


def find_multiplicative_inverse(K, q):
    inverse = 1
    while (K * inverse) % q != 1:
        inverse = inverse + 1
    return inverse


# DRIVER FUNCTION
print("\n\n### ELGAMAL CRYPTO SYSTEM ###\n\n")
# Prime number input
print("Inputs:")
q = int(input("\t-> Enter the prime number (q) = "))
primitive_root = int(input("\t-> Enter the primitive root (alpha) = "))
# Key generation
print("\nKey generation by A:")
private_key_of_A = int(input("\t-> Enter the private key for A (xA) = "))
print(f"\t=> Public key for a (yA) = (alpha ^ xA) mod q")
public_key_of_A = find_mod(base=primitive_root, exponent=private_key_of_A, modulus=q)
print(f"\t   yA = ({primitive_root} ^ {private_key_of_A}) mod {q}")
print(f"\t   yA = {public_key_of_A}")
# Encryption by B, using A's public key
print("\nEncryption by B, using A's public key:")
plain_text = int(input("\t-> Enter the plain text (M) = "))
k = int(input("\t-> Enter the value of random integer (k) = "))
print("\t=> K = (yA ^ k) mod q")
K = find_mod(base=public_key_of_A, exponent=k, modulus=q)
print(f"\t   K = ({public_key_of_A} ^ {k}) mod {q}")
print(f"\t   K = {K}")
print("\t=> Public key (c1) = (alpha ^ k) mod q")
c1 = find_mod(base=primitive_root, exponent=k, modulus=q)
print(f"\t   c1 = ({primitive_root} ^ {k}) mod {q}")
print(f"\t   c1 = {c1}")
print("\t=> Encrypted message (c2) = (K * M) mod m")
c2 = find_mod(base=K * plain_text, exponent=1, modulus=q)
print(f"\t   c2 = ({K} * {plain_text}) mod {q}")
print(f"\t   c2 = {c2}")
print(f"\nCIPHER TEXT = (c1, c2) = ({c1}, {c2})\n")
# Decryption by A, using A's private key
print("Decryption by A, using A's private key:")
print("\t=> K = (c1 ^ xA) mod q")
K = find_mod(base=c1, exponent=private_key_of_A, modulus=q)
print(f"\t   K = ({c1} ^ {private_key_of_A}) mod {q}")
print(f"\t   K = {K}")
print("\t=> Plain text (M) = (c2 * (K^-1)) mod q")
print("\t   M = (c2 mod q) * (K^-1) mod q")
multiplicative_inverse = find_multiplicative_inverse(K, q)
print(f"\t    -> Multiplicative inverse of K = {multiplicative_inverse}")
print("\t   M = (c2 mod q) * (K * Multiplicative inverse) mod q")
print("\t   M = (c2 * K * Multiplicative inverse) mod q")
print(f"\t   M = ({c2} * {K} * {multiplicative_inverse}) mod {q}")
M = find_mod(base=c2 * K * multiplicative_inverse, exponent=1, modulus=q)
print(f"\t   M = {M}")
# Footer
print("\n\nDEVANSHU GUPTA 21BCE0597\n\n")