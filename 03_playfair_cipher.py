def create_table(plain_text):
    table = []
    remaining_alphabets = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    appended_letters = ""
    # J and I are used in same cell, so replace J with I
    plain_text = plain_text.replace("J", "I")
    # Adding each letter from the plain text
    for letter in plain_text:
        if letter not in appended_letters:
            table.append(letter)
            remaining_alphabets.replace(letter, "")
            appended_letters = appended_letters + letter
    # Adding the remaining alphabets
    for alphabet in remaining_alphabets:
        if alphabet not in appended_letters:
            table.append(alphabet)
            appended_letters = appended_letters + alphabet
    # Creating the 5 x 5 matrix
    playfair_table = []
    for _ in range(5):
        playfair_table.append(list(table[0:5]))
        del table[0:5]
    # Print the table
    for row in playfair_table:
        print(row)
    # Return the table
    return playfair_table


def find_index_from_table(playfair_table, char):
    position = []
    row = -1
    for full_row in playfair_table:
        row = row + 1
        if char in full_row:
            col = full_row.index(char)
            position.append(row)
            position.append(col)
            break
    return position


def fairplay_cipher_encryption(plain_text, playfair_table):
    # Edit the plain text
    i = 0
    while i + 1 < len(plain_text):
        if plain_text[i] == plain_text[i + 1]:
            plain_text = plain_text[:i + 1] + "X" + plain_text[i + 1:]
        i = i + 1
    if len(plain_text) % 2 != 0:
        plain_text = plain_text + "X"
    print(f"\n-> Edited plain text: {plain_text}")
    # Divide plain text into pairs
    pairs = []
    for _ in range(len(plain_text) // 2):
        pairs.append(plain_text[:2])
        plain_text = plain_text[2:]
    print("\n-> List of pairs:")
    print(pairs)
    # Start encryption
    encrypted_text = ""
    for pair in pairs:
        # Extract the index of the characters
        letter_1_position = find_index_from_table(playfair_table=playfair_table, char=pair[0])
        letter_2_position = find_index_from_table(playfair_table=playfair_table, char=pair[1])
        # Find the encrypting character 
        if letter_1_position[0] == letter_2_position[0]:
            letter_1_col_new = (letter_1_position[1] + 1) % 5
            letter_1_row_new = letter_1_position[0]
            letter_2_col_new = (letter_2_position[1] + 1) % 5
            letter_2_row_new = letter_2_position[0]
        elif letter_1_position[1] == letter_2_position[1]:
            letter_1_row_new = (letter_1_position[0] + 1) % 5
            letter_1_col_new = letter_1_position[1]
            letter_2_row_new = (letter_2_position[0] + 1) % 5
            letter_2_col_new = letter_2_position[1]
        else:
            letter_1_col_new = letter_2_position[1]
            letter_1_row_new = letter_1_position[0]
            letter_2_col_new = letter_1_position[1]
            letter_2_row_new = letter_2_position[0]
        # Update the encrypted text
        encrypted_text = encrypted_text + playfair_table[letter_1_row_new][letter_1_col_new]
        encrypted_text = encrypted_text + playfair_table[letter_2_row_new][letter_2_col_new]
    # Retur the final encrypted message
    return encrypted_text


print("\n\n")
# Get the plain text
plain_text = input("-> Enter the plain text: ") # secret message
plain_text = plain_text.upper()
plain_text = plain_text.replace(" ", "")
# Create the table
print("\n-> Playfair Matrix:")
playfair_table = create_table(plain_text)
# Encrypt the text using Fairplay Cipher
cipher_text = fairplay_cipher_encryption(plain_text=plain_text, playfair_table=playfair_table)
print(f"\n\n=> The encrypted text is: {cipher_text}")

# Footer
print("\n\nDevanshu Gupta 21BCE0597\n\n")
