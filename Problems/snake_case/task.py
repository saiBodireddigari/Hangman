word = input()

for letter in word:
    if letter.isupper():
        index = word.index(letter)
        if index != 0:
            first_word = word[:index]
            sec_word = word[index + 1:]
            word = first_word + '_' + letter.lower() + sec_word

print(word)
