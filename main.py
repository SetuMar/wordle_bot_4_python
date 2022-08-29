word_list = open('wordleanswers.txt')
# open wordlist and read
words_to_search = []
number_of_guesses = 0
# define words to search and number of guesses

start_words = ['salet', 'crony', 'fight', 'khoum']
# define the guesses

for word in word_list:
    to_add = word.strip("\n")
    words_to_search.append(to_add)
    # add words to the list of possible words to search

while number_of_guesses != 6:
    if len(words_to_search) > 10:
        current_guess = start_words[number_of_guesses]
        # check if there are more than 10 possible guesses
    else:
        options = words_to_search
        options_score = {}

        current_option = ""
        current_highest = -1

        for word_index, word in enumerate(options):
            word_score = 0
            for letter in word:
                for word_check_index, word_to_check in enumerate(options):
                    if letter in word_to_check and word_to_check.count(letter) <= word.count(letter) and letter is not word[word_check_index]:
                        word_score += 1 / (word.count(letter) / word_to_check.count(letter))
                    elif word is not word_to_check and not (word_to_check.count(letter) >= word.count(letter) or word_to_check.count(
                                letter) <= word.count(letter)):
                        if letter is word_to_check[word_index]:
                            word_score += 2

        # loop through all letters of word and compare how similar they are to the other words by scoring words
        # add 1 if a letter is yellow (divided by the number of times the letter shows up in the curren word in comparison to the other words)
        # add 2 if the letter is green 

            options_score.update({word: word_score})
            for key, value in options_score.items():
                if value > current_highest:
                    current_option = key
                    # get the highest valued word
        current_guess = current_option
        # set the current guess to the high word

        if current_guess in words_to_search:
            words_to_search.pop(words_to_search.index(current_guess))
            # if it is in the words to search list, then remove the current guess

    print("Green = g, Yellow = y, grey = r")
    print("Please use the legend above to fill in your results from the wordle: ")
    print(current_guess)
    results = input()
    # ask user to input the results of guess suggested

    for letter_index, letter in enumerate(current_guess):
        current_letter_index = letter_index
        for search_word_index, word in enumerate(words_to_search):
            if word != "":
                if results[letter_index] == "g" and (current_guess[current_letter_index] != word[current_letter_index] or current_guess[current_letter_index] not in word):
                    words_to_search[search_word_index] = ""

                elif results[letter_index] == "r":
                    if current_guess.count(letter) == 1:
                        if current_guess[current_letter_index] in word:
                            words_to_search[search_word_index] = ""
                    else:
                        if current_guess[current_letter_index] is word[current_letter_index]:
                            words_to_search[search_word_index] = ""

                elif results[letter_index] == "y":
                    in_word = letter
                    if letter not in word or word[current_letter_index] is letter:
                        words_to_search[search_word_index] = ""

    num_of_posses = 0
    new_words = []
    for word in words_to_search:
        if word != "":
            new_words.append(word)

    # remove all words which do not correlated with wordle's rules

    words_to_search = new_words
    print(words_to_search)

    number_of_guesses += 1
    # increase the number of guesses value
