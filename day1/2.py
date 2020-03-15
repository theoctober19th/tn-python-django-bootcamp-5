words = input("Enter a list of words: ").split()
vowels = ('a', 'e', 'i', 'o', 'u')

for word in words:
    if word[0] in vowels and word[-1] in vowels:
        print(word, end=' ')
