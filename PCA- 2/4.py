import string
text = input("Enter a string: ")
v_count = 0
c_count = 0
d_count = 0
p_count = 0
vowels = "aeiouAEIOU"
punctuation = string.punctuation
for char in text:
    if char.isdigit():
        d_count += 1
    elif char in vowels:
        v_count += 1
    elif char.isalpha():
        c_count += 1
    elif char in punctuation:
        p_count += 1
print("\nNumber of vowels:", v_count)
print("Number of consonants:", c_count)
print("Number of digits:", d_count)
print("Number of punctuation marks:", p_count)
