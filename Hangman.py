#Game set up
import random
with open('words_alpha.txt') as word_file:
    valid_words = list(word_file.read().split())

play = 'y'
games_played = 0
wins = 0
losses = 0
random.shuffle(valid_words)


#create a definition to find where a letter appears in the word
#change and return word_display with the found letters
#remove a guess if neccessary. Also give feedback about this
def guess(letter):
    list_of_guesses.append(letter)
    global guesses
    global word_display
    letters_location = [position for position, char in enumerate(word) if char == letter]
    for pos in letters_location:
        word_display = word_display[:pos] + letter + word_display[pos+1:]
    if letter in word:
        print("Good guess!\nYour word is: " + word_display)
    else:
        print("Better luck next time!\nYour word is still: " + word_display)
        guesses = guesses -1
    return len(letters_location)
    print(" \n")




while play == 'y':
    #random.shuffle(valid_words)
    word = valid_words[games_played]
    #word = 'iii'
    print(word)
    guesses = 7
    yesorno = 1
    word_display = "_" * len(word)
    print("The word selected has " + str(len(word)) + ' letters')
    print(word_display)
    print("You have seven guesses. You only loose a guess if you guess a wrong letter")
    list_of_guesses = []
    word = word.lower()


    #create while loop with input that leads to calling function above. Input will check for str type.
    #check if word_display == word, if so, tell them they win and break the loop
    #check if guesses == 0, if so, tell them they lost
    while guesses > 0 and word_display != word:
        print("You have " + str(guesses) + " guesses left")
        print("Guesses: " + str(list_of_guesses))
        letter = input("What letter would you like to guess?   ")
        letter = letter.lower()
        if letter.isalpha() == False or len(letter) != 1 or letter in list_of_guesses:
            print("Input not a letter or already guessed. Try again")
            continue
        guess(letter)
        if word_display == word:
            print("Correct! You Won!\nThe word is: " + word_display)
            wins += 1
            break
        if guesses == 0:
            print("You have used all of your guesses...\n*Kicks stool out from under you* :(")
            losses += 1
            break

    #add loop that asks if you want to play again but only accepts y/n
    while yesorno == 1:
        play = input("Would you like to play again? (y/n)")
        play = play.lower()
        if (play != 'y') and (play != 'n'):
            print('Input incorrect. Answer with "y" or "n"')
            continue
        else:
            yesorno = 0
    games_played += 1

print("Games Played: " + str(games_played))
print("Wins: " + str(wins))
print("Losses : " + str(losses))