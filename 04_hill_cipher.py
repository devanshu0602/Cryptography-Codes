def clean_plain_text(plain_text):
    # Remove the whitespaces
    plain_text = plain_text.replace(" ", "")
    # Make it upper case
    plain_text = plain_text.upper()
    # Add 'X' between repeated letters
    i = 0
    while i + 1 < len(plain_text):
        if plain_text[i] == plain_text[i + 1]:
            plain_text = plain_text[:i + 1] + "A" + plain_text[i + 1:]
        i = i + 1
    # Add 'X' at the end if length of plain text is odd
    if len(plain_text) % 2 != 0:
        plain_text = plain_text + "A"
    print(f"-> Edited plain text: {plain_text}")
    return plain_text


def create_key_matrix(key):
    key = key.upper()
    n = int(len(key) ** 0.5)
    # Add number values of the letters
    matrix = []
    for letter in key:
        matrix.append(ord(letter) - ord('A'))
    # Reshape the matrix
    key_matrix = [matrix[: n], matrix[n :]]
    # Return the matrix
    return key_matrix


def create_plain_text_pairs(plain_text):
    pairs = []
    for i in range(0, len(plain_text), 2):
        pairs.append(plain_text[i : i + 2])
    return pairs


def hill_cipher(plain_text_pairs, key):
    # Find cipher text
    cipher_text = []
    for pair in plain_text_pairs:
        # eg: [WE] => [22, 4]
        number_pair = [ord(pair[0]) - ord('A'), ord(pair[1]) - ord('A')]
        print(f"Value of [{pair}] = {number_pair}")
        # Creating the encrypted number pair
        encrypted_pair = []
        # Matrix multiplication: [ key * number pair ]
        print(f"({key} * {number_pair}) mod 26")
        encrypted_pair.append(((key[0][0] * number_pair[0]) + (key[0][1] * number_pair[1])) % 26)
        encrypted_pair.append(((key[1][0] * number_pair[0]) + (key[1][1] * number_pair[1])) % 26)
        print(f"= {encrypted_pair}")
        encrypted_letter_1 = chr(encrypted_pair[0] + ord('A'))
        encrypted_letter_2 = chr(encrypted_pair[1] + ord('A'))
        print(f"=> [{pair}] = [{encrypted_letter_1 + encrypted_letter_2}]\n")
        # Finding the character associated to the number
        cipher_text.append(encrypted_letter_1)
        cipher_text.append(encrypted_letter_2)
    # Creating the encrypted text
    encrypted_text = "".join(cipher_text)
    # Return the encrypted text
    return encrypted_text
    

# Get the plain text
plain_text = input("\n\n-> Enter the plain text: ")
plain_text = clean_plain_text(plain_text=plain_text)
# Get the key
key = input("\n-> Enter the key to be used: ")
key_matrix = create_key_matrix(key=key)
for row in key_matrix:
    print(row)
# Create pairs of the plain text
plain_text_pairs = create_plain_text_pairs(plain_text=plain_text)
print(f"\n-> Pairs: {plain_text_pairs}")
# Find cipher text
print("\n\n### ENCRYPTION ###\n")
cipher_text = hill_cipher(plain_text_pairs=plain_text_pairs, key=key_matrix)
print(f"\n=> The encrypted text is: {cipher_text}")

# Footer
print("\nDevanshu Gupta 21BCE0597\n\n")