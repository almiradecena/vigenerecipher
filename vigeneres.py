P =    [0.082,0.015,0.028,0.043,0.127,0.022,0.020,0.061,0.070,0.002,
        0.008,0.040,0.024,0.067,0.075,0.019,0.001,0.060,0.063,0.091,
        0.028,0.010,0.023,0.001,0.020,0.001]

# Get repeating letters (frequency) in a string as a dictionary
def get_repeating_letters(string):
    repeating = {}
    for c in string:
        if c in repeating:
            repeating[c] += 1
        else:
            repeating[c] = 1   
    return repeating

# Get a list of substrings given a key length x
def get_substrings(string, x):
    substr = []
    for i in range(len(string)):
        if i < x:
            substr.append([string[i]])
            continue
        substr[i%x].append(string[i])
    return substr

# Get value closest to num  
def get_closest(arr, num):
    closest = arr[0]
    j = 0
    for i in range(len(arr)): 
        if(abs(0.065-arr[i]) < abs(0.065-closest)):
            closest = arr[i]
            j = i
    
    return closest, j

################### Getting Input ##########################
#ciph_tx = 'yswbhxdomstjwjfcbyldlwrnbthxanyskqhyldownydmwxetznfxbscmskrrkiwdsyrje' (From HW)

# Get cipher text
ciph_tx = input("Please Enter Ciphertext: ")
ciph_tx = ciph_tx.strip().lower()
while not ciph_tx.isalpha():
    print("Only letters (A-Z) please!")
    ciph_tx = input("Ciphertext: ")
    ciph_tx = ciph_tx.strip().lower()

# Get mode
mode = input("If you have the key, press 1\nIf you have the keylength, press 2: ")
while mode != '1' and mode != '2':
    print("Error! ")
    mode = input("If you have the key, press 1\nIf you have the keylength, press 2: ")
mode = int(mode)


################### Decrypt with Key  O(n) ##########################
#ciph_tx = netbfybzunmoqerlafmoqbxoalwld
 
if mode == 1:
    # Get key
    key = input("Input Key (Only letters A-Z): ")
    key = key.strip()
    while not key.isalpha():
        print("Only letters (A-Z) please!")
        key = input("Input Key (Only letters A-Z): ")
        key = key.strip()
    # Decrypt ciphertext
    i = 0
    plain_tx = ''
    for ch in ciph_tx:
        temp = ((ord(ch)-97) - (ord(key[i])-97)) % 26
        plain_tx += chr(temp + 97)
        i = (i + 1) % len(key)
    print('Plaintext: ', plain_tx)
    exit()

################### Decrypt with known key length ##########################

# Get key length
key_len = input("Input Keylength (Only digits): ")
while not key_len.isdigit():
    print("Error!")
    key_len = input("Input Keylength (Only digits): ")
key_len = int(key_len)

# Get substrings
substr = get_substrings(ciph_tx, key_len)

final_key = ''
for subs in substr:
    n = len(subs)
    repeating_letters = get_repeating_letters(subs)
    
    # Calculate frequency/len
    f_ig = []
    for i in range(0,26):
        c = chr(i+97)
        
        # Calculating repeated letters in y_i
        frequency = 0
        if c in repeating_letters:
            frequency = repeating_letters[c]
        f_ig.append(frequency)

    # Calculating m_g  
    final_mg = []
    for k in range(0,26):
        m_g = 0
        for i in range(0,26):
            f_index = (i+k)%26
            m_g += (1/n) * P[i] * f_ig[f_index]

        final_mg.append(m_g) 

    closest, j = get_closest(final_mg, 0.065)       # get closest m_g to 0.065 and it corresponds to character j
    final_key += (chr(j+97))
        
print("Your key is: ", final_key)

