text = input("Enter a string: ")
words = text.split()
abbreviation = ""
for word in words:
    abbreviation += word[0].upper() + ". "
abbreviation = abbreviation.strip()
print("\nFull abbreviation of the string:")
print(abbreviation)
