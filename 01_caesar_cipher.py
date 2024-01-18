def caesar_cipher_encryption(key, plain_text):
    # Declare empty string for encrypted text
    encrypted_text = ""
    for letter in plain_text:
        if letter.islower():
            encrypted_letter_ascii = ord('a') + ((ord(letter) - ord('a') + key) % 26)
            encrypted_letter = chr(encrypted_letter_ascii)
        elif letter.isupper():
            encrypted_letter_ascii = ord('A') + ((ord(letter) - ord('A') + key) % 26)
            encrypted_letter = chr(encrypted_letter_ascii)
        elif letter == " ":
            encrypted_text = encrypted_text + " "
            continue
        # Update the encrypted text
        encrypted_text = encrypted_text + encrypted_letter
    # Return the encrypted text
    return encrypted_text


def decryption(key, cipher_text):
    # Declare empty string for decrypted text
    decrypted_text = ""
    for letter in cipher_text:
        if letter.islower():
            shift = ord(letter) - ord('a') - key
            if shift < 0:
                shift = shift + 26
            decrypted_letter_ascii = ord('a') + (shift % 26)
            decrypted_letter = chr(decrypted_letter_ascii)
        elif letter.isupper():
            shift = ord(letter) - ord('A') - key
            if shift < 0:
                shift = shift + 26
            decrypted_letter_ascii = ord('A') + (shift % 26)
            decrypted_letter = chr(decrypted_letter_ascii)
        # Update the decrypted text
        if letter == " ":
            decrypted_text = decrypted_text + " "
        else:
            decrypted_text = decrypted_text + decrypted_letter
    # Return the decrypted text
    return decrypted_text


# Get the plain text
plain_text = input("\n\nEnter the plain text: ")
# Get the key value
key = int(input("Enter the key value: "))
# Make sure key value is between 1 and 25
while key < 1 and key > 25:
    print("Invalid key value.")
    key = int(input("Enter the key value: "))
# Encrypt the text using Caesar Cipher
cipher_text = caesar_cipher_encryption(key=key, plain_text=plain_text)
print(f"\n-> The encrypted text is: {cipher_text}")

print("\n\n")

# Get the cipher text
cipher_text = input("Enter the cipher text: ")
# Get the key value
key = int(input("Enter the key value: "))
# Make sure key value is between 1 and 25
while key < 1 and key > 25:
    print("Invalid key value.")
    key = int(input("Enter the key value: "))
# Decrypt the cipher text
decrypted_text = decryption(key=key, cipher_text=cipher_text)
print(f"\n-> The decrypted text is: {decrypted_text}")

# Footer
print("\nDevanshu Gupta 21BCE0597\n\n")




