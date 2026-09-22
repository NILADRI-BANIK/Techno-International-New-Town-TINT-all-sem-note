n = input("Enter a string: ")
r = ""
for char in n:
    if char.isalpha():
        if char == 'z':
            r += 'a'
        elif char == 'Z':
            r += 'A'
        else:
            r += chr(ord(char) + 1)  
    else:
        r += char  
print("String after converting each alphabetical character to the next letter:")
print(r)
