# Write your code here
import random

print("H A N G M A N")
print("")
code_list = ["python", "java", "kotlin"]
rand_word = random.choice(code_list)
replacement_value = "-"
word_dis = ""
last_range = 9
str1 = ""
counter_list = []
pieces_word = rand_word[0:len(rand_word)]
for x in pieces_word:
    word_dis += replacement_value


def list_to_string(st):
    str1 = ""
    for a in st:
        str1 += a
    return str1


replacement_list = list(word_dis)
list_rand = list(rand_word)

menu = input('Type "play" to play the game, "exit" to quit:')

if menu == 'play':
    while last_range:
        word_form = list_to_string(replacement_list)
        if word_form == rand_word:
            print(word_form)
            print("You guessed the word!")
            print("You survived!")
            print("")
            break
        print(word_form)
        letter = input("Input a letter: ")
        indices_to_replace = []
        if (letter in rand_word) and (letter not in word_form):
            counter_list.append(letter)
            print("")
            for i, y in enumerate(list_rand):
                if y == letter:
                    indices_to_replace += [i]
                    for x in indices_to_replace:
                        replacement_list[x] = letter
        elif letter in counter_list:
            print("You already typed this letter")
            counter_list.append(letter)
            if last_range == 1:
                print("You are hanged!")
                print("")
                break
            else:
                print("")
        elif len(letter) > 1:
            print("You should input a single letter")
            if last_range == 1:
                print("You are hanged!")
                print("")
                break
            else:
                print("")
        elif letter.isupper() or not (letter.isalpha()):
            print("It is not an ASCII lowercase letter")
            counter_list.append(letter)
            if last_range == 1:
                print("You are hanged!")
                print("")
                break
            else:
                print("")
        else:
            last_range = last_range - 1
            print("No such letter in the word")
            counter_list.append(letter)
            if last_range == 1:
                print("You are hanged!")
                print("")
                break
            else:
                print("")