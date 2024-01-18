alphabets = [
    'A', 'B', 'C', 'D', 'E', 
    'F', 'G', 'H', 'I', 'J', 
    'K', 'L', 'M', 'N', 'O', 
    'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z'
]


def monoalphabetic_cipher(plain_text, key):
    # Remove the whitespaces
    plain_text = plain_text.replace(" ", "")
    # Make it upper case
    plain_text = plain_text.upper()
    # Find cipher text
    cipher_text = []
    for letter in plain_text:
        index_of_cipher_letter = alphabets.index(letter)
        cipher_text.append(key[index_of_cipher_letter])
    encrypted_text = "".join(cipher_text)
    # Return the encrypted text
    return encrypted_text


def decrypt(cipher_text, key):
    # Make it upper case
    cipher_text = cipher_text.upper()
    # Decrypt the text
    decrypted_text = []
    for letter in cipher_text:
        index_of_decrypted_letter = key.index(letter)
        decrypted_text.append(alphabets[index_of_decrypted_letter])
    plain_text = "".join(decrypted_text)
    # Return the decrypted text
    return plain_text
    

## ENCRYPTION ##
# Get the plain text
plain_text = input("\n\n-> Enter the plain text: ")
# Get the key -> ESWZGKYDVOQRXPNTILFCAHJBMU
key_str = input("\n-> Enter the key to be used: ")
key = []
for alphabet in key_str:
    key.append(alphabet)
# Find cipher text
cipher_text = monoalphabetic_cipher(plain_text=plain_text, key=key)
print(f"\n\n=> The encrypted text is: {cipher_text}")

## DECRYPTION ##
# Get the encrypted text
cipher_text = input("\n\n-> Enter the cipher text: ")
# Get the key -> ESWZGKYDVOQRXPNTILFCAHJBMU
key_str = input("\n-> Enter the key to be used: ")
key = []
for alphabet in key_str:
    key.append(alphabet)
# Find cipher text
plain_text = decrypt(cipher_text=cipher_text, key=key)
print(f"\n\n=> The decrypted text is: {plain_text}")

# Footer
print("\nDevanshu Gupta 21BCE0597\n\n")