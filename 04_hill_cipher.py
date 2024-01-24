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


def find_inverse(key):
    # inverse = Adj(key) / det(key) 
    det = (key[0][0] * key[1][1]) - (key[0][1] * key[1][0])
    # (det * x) mod 26 should be equal to 1
    # => (det mod 26) * (x mod 26)
    # => (det * ?) mod 26 = 1
    det = det % 26
    x = 0
    while ((det * x) % 26) != 1:
        x = x + 1
    adjoint = [
        [key[1][1], -key[0][1]], 
        [-key[1][0], key[0][0]]
    ]
    if adjoint[0][1] < 0:
        adjoint[0][1] = adjoint[0][1] + 26
    if adjoint[1][0] < 0:
        adjoint[1][0] = adjoint[1][0] + 26
    # inverse = (x * adjoint)
    row, col = 0, 0
    inverse = adjoint.copy()
    for row in range(2):
        for col in range(2):
            inverse[row][col] = adjoint[row][col] * x    
    # Return the Inverse
    return inverse


def create_text_pairs(text):
    pairs = []
    for i in range(0, len(text), 2):
        pairs.append(text[i : i + 2])
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


def decrypt(cipher_text_pairs, key):
    # Find decrypted text
    decrypted_text = []
    for pair in cipher_text_pairs:
        # eg: [WE] => [22, 4]
        number_pair = [ord(pair[0]) - ord('A'), ord(pair[1]) - ord('A')]
        print(f"Value of [{pair}] = {number_pair}")
        # Creating the decrypted number pair
        decrypted_pair = []
        # Matrix multiplication: [ key * number pair ]
        print(f"({key} * {number_pair}) mod 26")
        decrypted_pair.append(((key[0][0] * number_pair[0]) + (key[0][1] * number_pair[1])) % 26)
        decrypted_pair.append(((key[1][0] * number_pair[0]) + (key[1][1] * number_pair[1])) % 26)
        print(f"= {decrypted_pair}")
        decrypted_letter_1 = chr(decrypted_pair[0] + ord('A'))
        decrypted_letter_2 = chr(decrypted_pair[1] + ord('A'))
        print(f"=> [{pair}] = [{decrypted_letter_1 + decrypted_letter_2}]\n")
        # Finding the character associated to the number
        decrypted_text.append(decrypted_letter_1)
        decrypted_text.append(decrypted_letter_2)
    # Creating the decrypted text
    plain_text = "".join(decrypted_text)
    # Return the decrypted text
    return plain_text
    

print("\n\n### ENCRYPTION ###\n")
# Get the plain text
plain_text = input("\n\n-> Enter the plain text: ")
plain_text = clean_plain_text(plain_text=plain_text)
# Get the key
key = input("\n-> Enter the key to be used: ")
key_matrix = create_key_matrix(key=key)
for row in key_matrix:
    print(row)
# Create pairs of the plain text
plain_text_pairs = create_text_pairs(text=plain_text)
print(f"\n-> Pairs: {plain_text_pairs}\n")
# Find cipher text
cipher_text = hill_cipher(plain_text_pairs=plain_text_pairs, key=key_matrix)
print(f"\n=> The encrypted text is: {cipher_text}")


print("\n\n### DECRYPTION ###\n")
# Get the cipher text
cipher_text = input("\n\n-> Enter the cipher text: ")
# Find the inverse of the matrix
print("\n-> Key for decryption = Inverse(key)")
key_matrix_inverse = find_inverse(key=key_matrix)
print(f"=> Inverse(key) = {key_matrix_inverse}")
# Create pairs of the cipher text
cipher_text_pairs = create_text_pairs(text=cipher_text)
print(f"\n-> Pairs: {cipher_text_pairs}\n")
# Get the decrypted text
decrypted_text = decrypt(cipher_text_pairs=cipher_text_pairs, key=key_matrix_inverse)
print(f"\n=> The decrypted text is: {decrypted_text}")

# Footer
print("\nDevanshu Gupta 21BCE0597\n\n")
