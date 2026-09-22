t = input("Enter a string: ")
words = t.split()
m_words = [word for word in words if word.endswith("tion")]
print("Words ending with 'tion':")
if m_words:
    print(", ".join(m_words))
else:
    print("No words ending with 'tion' found.")
