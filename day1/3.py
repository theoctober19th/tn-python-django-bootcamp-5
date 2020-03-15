paragraph = input("Enter a paragraph: ")

sentences = paragraph.split('.')
length = len(sentences) - 1
print("There are", length, "sentences.")