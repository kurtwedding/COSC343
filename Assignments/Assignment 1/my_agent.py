__author__ = "Kurt Wedding-Speight"
__organization__ = "COSC343/AIML402, University of Otago"
__email__ = "wedku875@student.otago.ac.nz"

class WordleAgent:
    """
    A class that encapsulates the code dictating the
    behaviour of the Wordle playing agent

    ...

    Attributes
    ----------
    dictionary : list
        a list of valid words for the game
    letter : list
        a list containing valid characters in the game
    word_length : int
        the number of letters per guess word
    num_guesses : int
        the max. number of guesses per game
    mode: str
        indicates whether the game is played in 'easy' or 'hard' mode

    Methods
    -------
    AgentFunction(percepts)
        Returns the next word guess given state of the game in percepts
    """

    def __init__(self, dictionary, letters, word_length, num_guesses, mode):
        """
        :param dictionary: a list of valid words for the game
        :param letters: a list containing valid characters in the game
        :param word_length: the number of letters per guess word
        :param num_guesses: the max. number of guesses per game
        :param mode: indicates whether the game is played in 'easy' or 'hard' mode
        """

        self.dictionary = dictionary
        self.letters = letters
        self.word_length = word_length
        self.num_guesses = num_guesses
        self.mode = mode

    def AgentFunction(self, percepts):
        """Returns the next word guess given state of the game in percepts

        :param percepts: a tuple of three items: guess_counter, letter_indexes, and letter_states;
                guess_counter is an integer indicating which guess this is, starting with 0 for initial guess;
                letter_indexes is a list of indexes of letters from self.letters corresponding to
                            the previous guess, a list of -1's on guess 0;
                letter_states is a list of the same length as letter_indexes, providing feedback about the
                            previous guess (conveyed through letter indexes) with values of 0 (the corresponding
                            letter was not found in the solution), -1 (the corresponding letter is found in the
                            solution, but not in that spot), 1 (the corresponding letter is found in the solution
                            in that spot).
        :return: string - a word from self.possible_words that is the next guess, based on possible answers and
                statistics
        """

        # This is how you extract three different parts of percepts.
        guess_counter, letter_indexes, letter_states = percepts

        # Here's where you should put in your code

        nullLetters = []
        wrongLetters = []
        correctLetters = {}

        if guess_counter == 0:
            self.possible_words = list(self.dictionary)  # if no guesses have been made yet, reset the possible words
            self.guessed_words = []
            # to the dict
        else:
            # Code to add the letters to a list depending on if they are in the answer or not.
            for x in range(self.word_length):  # For each letter in the guess,
                if letter_states[x] == 1:  # If letter is in correct place
                    if self.letters[letter_indexes[x]] in nullLetters:
                        nullLetters.remove(self.letters[letter_indexes[x]])
                    correctLetters[self.letters[letter_indexes[x]]] = x

                elif letter_states[x] == 0:
                    if self.letters[letter_indexes[x]] not in wrongLetters:
                        if self.letters[letter_indexes[x]] not in correctLetters:  # if the
                            # letter is not in the solution and not in the wrong or right letters list
                            if self.letters[letter_indexes[x]] not in nullLetters:
                                nullLetters.append(self.letters[letter_indexes[x]])

                elif letter_states[x] == -1:  # if letter is in wrong place
                    if self.letters[letter_indexes[x]] in nullLetters:
                        nullLetters.remove(self.letters[letter_indexes[x]])
                    if self.letters[letter_indexes[x]] not in wrongLetters:
                        wrongLetters.append(self.letters[letter_indexes[x]])

            # Code to check if the letters are in the possible words, and to remove the words if the answer cannot be
            # them.
            for x in range(len(nullLetters)):
                y = 0
                while y < len(self.possible_words):  # using a while loop so that it can recheck an index if an
                    # element is removed
                    if y >= len(self.possible_words):
                        break
                    if nullLetters[x] in self.possible_words[y]:
                        self.possible_words.pop(y)
                    else:
                        y += 1

            for x in range(len(wrongLetters)):
                y = 0
                while y < len(self.possible_words):
                    if y >= len(self.possible_words):
                        break
                    if wrongLetters[x] not in self.possible_words[y]:
                        self.possible_words.pop(y)
                    else:
                        y += 1

            for x in correctLetters:
                y = 0
                while y < len(self.possible_words):
                    if y >= len(self.possible_words):
                        break
                    if x != self.possible_words[y][correctLetters[x]]:
                        self.possible_words.pop(y)
                    else:
                        y += 1

        # Here is the code to evaluate how many letters occur in the rest of the dictionary, and makes a guess
        # based off of that data.
        dataDict = {}
        wordDict = {}
        for letter in self.letters:  # create a dictionary of each letter in the alphabet
            dataDict[letter] = 0
        for word in self.possible_words:  # count up the number of each letter that occurs in the possible words
            wordDict[word] = 0
            for letter in word:
                dataDict[letter] += 1

        for word in wordDict:  # Value each word based on the occurrences of each of its letters
            for letter in range(len(word)):
                if word.count(word[letter]) <= 1:
                    if word.index(word[letter]) == letter:
                        wordDict[word] += dataDict[word[letter]]

        wordDict = sorted(wordDict.items(), key=lambda i: i[1], reverse=True)

        guess = wordDict[0][0]
        if guess_counter == 0:
            pass
        else:
            for index, word in enumerate(wordDict): # Code to not repeat guesses
                if word[0] not in self.guessed_words:
                    self.guessed_words.append(word[0])
                    guess = word[0]
                    break

        return guess
