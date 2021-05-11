## Get the longest repeated substring in a string
## https://www.geeksforgeeks.org/longest-repeating-and-non-overlapping-substring/
def longestRepeatedSubstring(str):
 
    n = len(str)
    LCSRe = [[0 for x in range(n + 1)]
                for y in range(n + 1)]
 
    res = "" # To store result
    res_length = 0 # To store length of result
 
    # building table in bottom-up manner
    index = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
             
            # (j-i) > LCSRe[i-1][j-1] to remove
            # overlapping
            if (str[i - 1] == str[j - 1] and
                LCSRe[i - 1][j - 1] < (j - i)):
                LCSRe[i][j] = LCSRe[i - 1][j - 1] + 1
 
                # updating maximum length of the
                # substring and updating the finishing
                # index of the suffix
                if (LCSRe[i][j] > res_length):
                    res_length = LCSRe[i][j]
                    index = max(i, index)
                 
            else:
                LCSRe[i][j] = 0
 
    # If we have non-empty result, then insert
    # all characters from first character to
    # last character of string
    if (res_length > 0):
        for i in range(index - res_length + 1,
                                    index + 1):
            res = res + str[i - 1]
 
    return res

## Get the factors of a number
## https://www.tutorialspoint.com/How-to-Find-Factors-of-Number-using-Python
def get_factors(num):
    factors=[]
    for i in range(1,num+1):
        if num%i==0:
            factors.append(i)
    return factors

# Get a list of substrings given a key length x
def get_substrings(string, x):
    substr = []
    for i in range(len(string)):
        if i < x:
            substr.append([string[i]])
            continue
        substr[i%x].append(string[i])
    return substr

# Get repeating letters (frequency) in a string as a dictionary
def get_repeating_letters(string):
    repeating = {}
    for c in string:
        if c in repeating:
            repeating[c] += 1
        else:
            repeating[c] = 1   
    return repeating

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

# Get longest repeated substring 
repeat = longestRepeatedSubstring(ciph_tx)

# Ensure repeated substring is longer than 1 letter long
if len(repeat) <= 1:
    print('Kasiski test failed!!!!!!!!!')
    exit()

first = ciph_tx.find(repeat, 0, len(ciph_tx))           # first occurence of repeated substring in string
second = ciph_tx.find(repeat, first+1, len(ciph_tx))    # second occurence of repeated substring in string

print('Repeated substring is ' + repeat + ' at', first, 'and', second)

multiple = second-first                                 
factors = get_factors(multiple)

ioc = []                                            # Closest ioc to 0.065 for all factors
for factor in factors: 
    # Get substrings for factor
    substrings = get_substrings(ciph_tx, factor)

    # Calculate index of coincidence for each factor
    factor_ioc = []                                 # Ioc for each factor
    for string in substrings:
        n = len(string)
        repeating_letters = get_repeating_letters(string)

        # Calculate index of coincidence
        frequency = 0
        for letter in repeating_letters:
            m = repeating_letters[letter]
            frequency += m*(m - 1)

        curr_ioc = (1/(n*(n-1)))*frequency          # Ioc for current substring
        factor_ioc.append(round(curr_ioc, 4)) 
    
    closest, _ = get_closest(factor_ioc, 0.065)     # closest ioc to 0.065
    ioc.append(closest)

closest, i = get_closest(ioc, 0.065)                # final closest ioc from all factors and factor it corresponds to
print(closest, factors[i])
print('Keyword length is ', factors[i])


