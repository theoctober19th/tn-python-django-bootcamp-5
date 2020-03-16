para = input("Enter a paragraph.")

sentences = para.split('.')
newlist = []
for sentence in sentences:
    newsentence = sentence.capitalize()
    newlist.append(newsentence)

newparagraph = '. '.join(newlist)

print(newparagraph)