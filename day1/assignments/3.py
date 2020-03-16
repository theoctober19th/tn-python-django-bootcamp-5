words = input('Enter a pragraph.').split(' ')

counts = {}

for word in words:
    if word[-1] == '.':
        word = word[:-1]
    word = word.lower()
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

for (word, freq) in counts.items():
     print(word, "=", freq)