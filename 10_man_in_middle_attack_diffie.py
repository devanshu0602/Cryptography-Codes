def get_public_numbers():
    P = int(input("\t-> Prime Number (P) = "))
    G = int(input("\t-> Base Number (G) = "))
    return P, G


def get_private_keys():
    private_key_alice = int(input("\t-> Alice's Private Key = "))
    private_key_bob = int(input("\t-> Bob's Private Key = "))
    x_d1 = int(input("\t-> C's Private Key 1 = "))
    x_d2 = int(input("\t-> C's Private Key 2 = "))
    return private_key_alice, private_key_bob, x_d1, x_d2


def find_mod(base, exponent, modulus):
    base = base % modulus
    remainder = 1
    while exponent > 0:
        if exponent % 2 == 1:
            remainder = (remainder * base) % modulus
        base = (base * base) % modulus
        exponent = exponent // 2
    return remainder


def generate_public_key(base_value, prime_number, private_key):
    print("\t= (G ^ Private Key) mod P")
    print(f"\t= ({base_value} ^ {private_key}) mod {prime_number}")
    remainder = find_mod(base=base_value, exponent=private_key, modulus=prime_number)
    print(f"\t= {remainder}")
    return remainder


def generate_shared_secret_key(base_value, prime_number, private_key):
    print("\t= (Public Key ^ Private Key) mod P")
    print(f"\t= ({base_value} ^ {private_key}) mod {prime_number}")
    remainder = find_mod(base=base_value, exponent=private_key, modulus=prime_number)
    print(f"\t= {remainder}")
    return remainder


# DRIVER FUNCTION
print("\n\n### DIFFIE HELLMAN KEY EXCHANGE ###\n\n")
# Global Numbers
print("Enter the Global Numbers:")
P, G = get_public_numbers()
# Alice's, Bob's, Third person's (C) Private Keys
print("\nEnter the Private Keys:")
private_key_alice, private_key_bob, x_d1, x_d2 = get_private_keys()
# Alice's and Bob's Public Key
print("\nGenerating the Public Keys:")
print("\t-> Alice's Public Key")
public_key_alice = generate_public_key(base_value=G, prime_number=P, private_key=private_key_alice)
print("\t-> Bob's Public Key")
public_key_bob = generate_public_key(base_value=G, prime_number=P, private_key=private_key_bob)
print("\t-> C's Public Key 1")
y_d1 = generate_public_key(base_value=G, prime_number=P, private_key=x_d1)
print("\t-> C's Public Key 2")
y_d2 = generate_public_key(base_value=G, prime_number=P, private_key=x_d2)
# Shared Secret Key
print("\nComputing the Secret Keys:")
print("\t-> Alice's Secret Key")
secret_key_alice = generate_shared_secret_key(base_value=y_d1, prime_number=P, private_key=private_key_alice)
print("\t-> C's Secret Key to replicate Alice's")
c_secret_key_alice = generate_shared_secret_key(base_value=public_key_alice, prime_number=P, private_key=x_d1)
if (secret_key_alice == c_secret_key_alice):
    print("\n=> WE CAN SEE THAT BOTH THE SECRET KEYS ARE SAME.")
    print(f"(Alice's Secret Key = C's Secret Key for Alice)\n")
else:
    print("\nERROR IN THE CALCULATIONS")
print("\t-> Bob's Secret Key")
secret_key_bob = generate_shared_secret_key(base_value=y_d2, prime_number=P, private_key=private_key_bob)
print("\t-> C's Secret Key to replicate Bob's")
c_secret_key_bob = generate_shared_secret_key(base_value=public_key_bob, prime_number=P, private_key=x_d2)
if (secret_key_bob == c_secret_key_bob):
    print("\n=> WE CAN SEE THAT BOTH THE SECRET KEYS ARE SAME.")
    print(f"(Bob's Secret Key = C's Secret Key for Bob)")
else:
    print("\nERROR IN THE CALCULATIONS")
# Footer
print("\n\nDevanshu Gupta 21BCE0597\n\n")