'''s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:2])
print(s[8:])
print(s[0:20])'''

'''print("String concatenation")
a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)
owoc = 'banan'
print('m' in owoc)
print('nan' in owoc)
if 'a' in owoc:
    print("O'k.")'''

'''gt = 'Hello John'
zap = gt.lower()
print(zap)
print(gt)
print('Hi There'.lower())
print('Hi There'.upper())'''

'''gt = 'Hello Bob'
print(gt)
nstr = gt.replace('Bob', 'Jane ')
print(nstr)
nstr = gt.replace('o', 'a')
print(nstr)'''

'''print("Stripping Whitespace")
gt = '  Hello Bob   '
print(gt.lstrip())
print(gt.rstrip())
print(gt.strip())'''

'''s = 'azcbobobezgghak1'
cStr = s[0]  # Initialize current substring to the first character
lon = s[0]   # Initialize longest substring to the first character

for i in range(1, len(s)):  # Start from the second character
    if s[i] >= cStr[-1]:  # Check if the current character is >= last character of current substring
        cStr += s[i]  # Append current character to the current substring
        if len(cStr) > len(lon):  # If current substring is longer than longest, update longest
            lon = cStr
    else:
        cStr = s[i]  # Reset current substring to the current character if it's not in order

print('Longest substring in alphabetical order is:', lon)'''

'''def count_vol(s):
    num_vol = 0
    vowels = 'aeiou'  # Define a string of vowels
    for char in s:
        if char in vowels:  # Check if the character is in the vowels list
            num_vol += 1  # Increment the count if it's a vowel
    print(num_vol)

# Test the function
count_vol('azcbobobegghakl')'''

# Function to count vowels in a string
'''def count_vol(s):
    num_vol = 0
    vowels = 'aeiou'  # Set of vowels
    for char in s:
        if char in vowels:
            num_vol += 1  # Increment count for each vowel
    return num_vol  # Return the total number of vowels

# Main block of code
s = 'Marek'
total = 0
for c in s:
    if c in 'aeiou':  # Check if the character is a vowel
        total += 1  # Increment the vowel count

print(u"Liczba samoglosek: " + str(total))  # Corrected string with Polish letters

# Print the vowel count from the string 'azcbobobegghaklaaa'
print("Count from count_vol function:", count_vol('azcbobobegghaklaaa'))'''

'''def jest_w(lit, wyraz):
    if wyraz == '':
        return False  # Return False for an empty string
    if len(wyraz) == 1:
        return wyraz == lit  # Return True if the single character matches

    index = len(wyraz) // 2  # Use integer division
    mLit = wyraz[index]  # Get the middle character

    if lit == mLit:
        return True  # Found the letter
    elif lit < mLit:
        return jest_w(lit, wyraz[:index])  # Search in the left half
    else:
        return jest_w(lit, wyraz[index + 1:])  # Search in the right half, skip middle

# Test the function
print(jest_w('a', 'baba'))  # Should return True
print(jest_w('c', 'baba'))  # Should return False

'''



