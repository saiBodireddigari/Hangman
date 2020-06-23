sentance = input()
vowels = "aeiou"


for letter in sentance:
    bool_var = letter.isalpha()
    if letter in vowels:
        print("vowel")
    elif not bool_var:
        break
    else:
        print("consonant")
