def key_generation(key):
    # P10(Key)
    p10 = list(input("\n\tEnter P10 value: ").split(" ")) # 3 5 2 7 4 10 1 9 8 6
    p10_key = [key[int(i) - 1] for i in p10]
    print(f"\t-> After P10 = {' '.join(map(str, p10_key))}")
    
    # Divide P10(Key) into left and right and LS-1 
    p10_key_left = p10_key[:5]
    p10_key_right = p10_key[5:]
    print("\n\tApplying Left Shift - 1")
    ls1_p10_key_left = p10_key_left[1:] + p10_key_left[:1]
    ls1_p10_key_right = p10_key_right[1:] + p10_key_right[:1]
    ls1_p10_key = ls1_p10_key_left + ls1_p10_key_right
    print(f"\t-> After LS-1 = {' '.join(map(str, ls1_p10_key))}")
    
    # P8(LS-1)
    p8 = list(input("\n\tEnter P8 value: ").split(" ")) # 6 3 7 4 8 5 10 9
    p8_ls1_p10_key = [ls1_p10_key[int(i) - 1] for i in p8]
    print(f"\t-> After P8 = {' '.join(map(str, p8_ls1_p10_key))}")
    
    # Key 1 = Value after P8
    key1 = p8_ls1_p10_key.copy()
    print(f"\n\t===> Key-1 = {' '.join(map(str, p8_ls1_p10_key))}")
    
    # LS-2 on LS-1(P10(Key))
    print("\n\tApplying Left Shift - 2")
    ls2_ls1_p10_key_left = ls1_p10_key_left[2:] + ls1_p10_key_left[:2]
    ls2_ls1_p10_key_right = ls1_p10_key_right[2:] + ls1_p10_key_right[:2]
    ls2_ls1_p10_key = ls2_ls1_p10_key_left + ls2_ls1_p10_key_right
    print(f"\t-> After LS-2 = {' '. join(map(str, ls2_ls1_p10_key))}")
    
    # P8(LS-2)
    p8_ls2_ls1_p10_key = [ls2_ls1_p10_key[int(i) - 1] for i in p8]
    print(f"\n\t-> After P8 = {' '.join(map(str, p8_ls2_ls1_p10_key))}")
    
    # Key 2 = Value after P8
    key2 = p8_ls2_ls1_p10_key.copy()
    print(f"\n\t===> Key-2 = {' '.join(map(str, p8_ls2_ls1_p10_key))}")
    
    # Return the keys
    return key1, key2


def mid_function(subkey, exp_perm_input, exp_perm, sbox0, sbox1, p4):
    # Expansion permutation
    print(f"\n\t-> Expansion Permutation input = {' '.join(map(str, exp_perm_input))}")
    ep_output = [exp_perm_input[int(i) - 1] for i in exp_perm]
    print(f"\t-> Expansion Permutation output = {' '.join(map(str, ep_output))}")
    
    # EP_output XOR subkey
    print("\n\tSubkey XOR Expansion Permutation output:")
    XOR_output = [str((int(ep_output[i]) + int(subkey[i])) % 2) for i in range(len(subkey))]
    XOR_output_left = XOR_output[:4]
    XOR_output_right = XOR_output[4:]
    print(f"\t-> XOR operation output = {' '. join(map(str, XOR_output))}")
    
    # s-Box 0
    print(f"\n\t-> sBox-0 input = {' '.join(map(str, XOR_output_left))}")
    sbox0_row = int(str(XOR_output_left[0] + XOR_output_left[3]), 2)
    sbox0_col = int(str(XOR_output_left[1] + XOR_output_left[2]), 2)
    sbox0_val = sbox0[sbox0_row][sbox0_col]
    print(f"\t-> sBox-0 value = sbox0[{sbox0_row}][{sbox0_col}] = binary_of({sbox0_val}) = ", end="")
    sbox0_val = format(int(sbox0_val), '02b')
    print(f"{' '.join(map(str, sbox0_val))}")

    # s-Box 1
    print(f"\n\t-> sBox-1 input = {' '.join(map(str, XOR_output_right))}")
    sbox1_row = int(str(str(XOR_output_right[0]) + str(XOR_output_right[3])), 2)
    sbox1_col = int(str(str(XOR_output_right[1]) + str(XOR_output_right[2])), 2)
    sbox1_val = sbox1[sbox1_row][sbox1_col]
    print(f"\t-> sBox-1 value = sbox1[{sbox1_row}][{sbox1_col}] = binary_of({sbox1_val}) = ", end="")
    sbox1_val = format(int(sbox1_val), '02b')
    print(f"{' '.join(map(str, sbox1_val))}")

    # P4(sbox0 + sbox1)
    p4_input = str(str(sbox0_val) + str(sbox1_val))
    print(f"\n\t-> P4 input = {' '.join(map(str, p4_input))}")
    p4_output = [p4_input[int(i) - 1] for i in p4]
    print(f"\t-> P4 output = {' '.join(map(str, p4_output))}")

    # Return P4 output as result
    return p4_output
    

def sDES_encryption(key1, key2):
    # Plain text
    plain_text = list(input("\n\tEnter the plain text: ").split(" ")) # 1 1 1 1 0 0 1 1
    
    # Initial Permutation
    ip = list(input("\n\tEnter Initial Permutation value: ").split(" ")) # 2 6 3 1 4 8 5 7
    ip_pt = [plain_text[int(i) - 1] for i in ip]
    print(f"\t-> Initial Permutation output = {' '.join(map(str, ip_pt))}")

    # Inputs for Function
    # Expansion Permutation
    exp_perm = list(input("\n\tEnter the Expansion Permutation value: ").split(" ")) # 4 1 2 3 2 3 4 1
    # s-box 0
    print("\n\tEnter sBox-0 values:") # 1 0 3 2, 3 2 1 0, 0 2 1 3, 3 1 3 2
    sbox0 = []
    for i in range(4):
        sbox0_row = list(input("\t").split(" "))
        sbox0.append(sbox0_row)
    # s-box 1
    print("\n\tEnter sBox-1 values:") # 0 1 2 3, 2 0 1 3, 3 0 1 0, 2 1 0 3
    sbox1 = []
    for i in range(4):
        sbox1_row = list(input("\t").split(" "))
        sbox1.append(sbox1_row)
    # P4
    p4 = list(input("\n\tEnter P4 value: ").split(" ")) # 2 4 3 1
    
    # Function_k 
    ip_pt_left = ip_pt[:4]
    ip_pt_right = ip_pt[4:]
    print("\n\t| Function_k: E/P -> XOR -> Sbox0 and Sbox1 -> P4 |")
    p4_f1_result = mid_function(subkey=key1, exp_perm_input=ip_pt_right, exp_perm=exp_perm, sbox0=sbox0, sbox1=sbox1, p4=p4) # used in IP inverse
    print("\n\t|                End of Function_k                |")

    # IP(PT) XOR Func1_output
    switch_output_right = [str(((int(ip_pt_left[i]) + int(p4_f1_result[i])) % 2)) for i in range(len(ip_pt_left))]
    print(f"\n\t->SW left input = SW right output = {' '.join(map(str, switch_output_right))}")
    switch_output_left = ip_pt_right.copy()
    print(f"\t->SW right input = SW left output = {' '.join(map(str, switch_output_left))}")

    # Function_k
    print("\n\t| Function_k: E/P -> XOR -> Sbox0 and Sbox1 -> P4 |")
    p4_f2_result = mid_function(subkey=key2, exp_perm_input=switch_output_right, exp_perm=exp_perm, sbox0=sbox0, sbox1=sbox1, p4=p4)
    print("\n\t|                End of Function_k                |")

    # SW left output XOR Func2_output
    print(f"\n\tP4 output XOR IP(PT)_right:")
    ip_inverse_left_input = [str((int(switch_output_left[i]) + int(p4_f2_result[i])) % 2) for i in range(len(switch_output_left))]
    print(f"\t-> XOR output = {' '.join(map(str, ip_inverse_left_input))}")

    # IP inverse
    ip_inverse = list(input("\n\tEnter IP inverse value: ").split(" ")) # 4 1 3 5 7 2 8 6
    print(f"\n\tIP inverse(XOR_output + SW right output):")
    ip_inverse_input = ip_inverse_left_input + switch_output_right
    print(f"\t-> IP inverse input = {' '.join(map(str, ip_inverse_input))}")
    ip_inverse_output = [ip_inverse_input[int(i) - 1] for i in ip_inverse]
    print(f"\t-> IP inverse output = {' '.join(map(str, ip_inverse_output))}")
    # Return result
    return ip_inverse_output


# DRIVER FUNCTION
print("\n\n### s-DES KEY GENERATION AND ENCRYPTION ###\n\n")
# Key generation
print("--> Key Generation:")
k = list(input("\n\tEnter the key: ").split(" ")) # 1 1 0 0 0 1 1 1 1 0
k1, k2 = key_generation(key=k)
# Encryption
print("\n\n--> s-DES Encryption")
cipher_text = sDES_encryption(key1=k1, key2=k2)
print(f"\n\n !! CIPHER TEXT = {' '.join(map(str, cipher_text))} !!")
# Footer
print("\n\nDevanshu Gupta 21BCE0597\n\n")