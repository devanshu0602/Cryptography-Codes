S_BOX = [
	0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
	0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
	0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
	0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
	0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
	0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
	0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
	0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
	0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
	0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
	0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
	0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
	0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
	0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
	0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
	0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

ROUND_CONSTANTS = [
	0x00000000, 0x01000000, 0x02000000, 0x04000000,
	0x08000000, 0x10000000, 0x20000000, 0x40000000,
	0x80000000, 0x1b000000, 0x36000000
]


# Left shift 1
def find_rotword(word):
	return word[1:] + word[:1]


# SBOX byte substitution
def find_subword(word):
	sub_word = ()
	# Loop through the current word
	for i in range(4):
		# Get row value
		if word[i][0].isdigit() == False:
			row = ord(word[i][0]) - 86
		else:
			row = int(word[i][0]) + 1
		# Get column value
		if word[i][1].isdigit() == False:
			col = ord(word[i][1]) - 86
		else:
			col = int(word[i][1]) + 1
		# Get the index based on row and col
		s_box_value_index = (row * 16) - (17 - col)
		# Get the value from sbox
		piece = hex(S_BOX[s_box_value_index])[2:]
		# Check length to ensure 0 padding
		if len(piece) != 2:
			piece = '0' + piece
		# Create a tuple
		sub_word = (*sub_word, piece)
	# Return string
	return ''.join(sub_word)


# Hex to Binary conversion
def hex_to_binary(hex):
	return bin(int(str(hex), 16))


# Hex1 XOR Hex2
def find_XOR_value(hex1, hex2):
	# Convert to binary
	bin1 = hex_to_binary(hex1)
	bin2 = hex_to_binary(hex2)
	# Calculate the XOR value
	XOR_result = int(bin1, 2) ^ int(bin2, 2)
	# Cut prefix (0x00 to 00)
	XOR_result = hex(XOR_result)[2:]
	# 0 padding if length not equal to 8
	if len(XOR_result) != 8:
		XOR_result = '0' + XOR_result
    # Return XOR value
	return XOR_result

# Key expansion function
def key_expansion(key):
	# Create list to hold all words
	all_words = [()] * 44
	# Add first 4 words
	for i in range(4):
		all_words[i] = (
			key[4 * i], 
		    key[(4 * i) + 1], 
			key[(4 * i) + 2], 
			key[(4 * i) + 3]
		)
    # Add results of g function computation
	for i in range(4, 44):
		# Get required previous words
		subkey_fourth_word = all_words[i - 1]
		subkey_first_word = all_words[i - 4]
		# G function
		if i % 4 == 0:
			# LS-1
			rot_word = find_rotword(subkey_fourth_word)
			# Sbox byte substitution
			sub_word = find_subword(rot_word)
			# Get round constant value
			round_const = ROUND_CONSTANTS[int(i / 4)]
			# XOR of subword and round_constant
			subkey_fourth_word = find_XOR_value(sub_word, hex(round_const)[2:]) 
		# Creating strings of hex
		subkey_first_word = ''.join(subkey_first_word)
		subkey_fourth_word = ''.join(subkey_fourth_word)
		# XOR of subkey_first_word and g_func_output
		subkey_value = find_XOR_value(subkey_first_word, subkey_fourth_word)
		all_words[i] = (subkey_value[:2], subkey_value[2:4], subkey_value[4:6], subkey_value[6:8])
    # Return the result
	return all_words


def create_subkeys(words):
	subkeys = []
	# Loop through the words in groups of 4 to create subkeys
	for i in range(0, len(words), 4):
		# Transpose the words within the subkey
		transposed_subkey = "".join("".join(word[j] for word in words[i:i+4]) for j in range(4))
		# Add space between values for easier reading
		spaced_subkey = " ".join(transposed_subkey[i:i+2] for i in range(0, len(transposed_subkey), 2))
		# Add subkey to list
		subkeys.append(spaced_subkey)
	# Return all subkeys
	return subkeys


# DRIVER FUNCTION
print("\n\n### AES KEY EXPANSION ###\n\n")
# Key input
key = list(input("\tEnter the key value: ").split(" ")) # 73 61 74 69 73 68 63 6a 69 73 62 6f 72 69 6e 67
# Key expansion
all_words = key_expansion(key=key)
# Convert to subkeys
subkeys = create_subkeys(words=all_words)
print("\n\n\tAll Subkeys:\n")
for i in range(len(subkeys)):
	print(f"\t-> Subkey {i} = {subkeys[i]}")
# Footer
print("\n\nDevanshu Gupta 21BCE0597\n\n")