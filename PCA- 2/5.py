t = input("Enter a string: ")
p_text = t.lower()
if p_text == p_text[::-1]:
    print(t,"is a Palindrome.")
else:
    print(t,"is not a Palindrome.")
