__author__ = "Kurt Wedding-Speight"
__organization__ = "COSC343/AIML402, University of Otago"
__email__ = "kurtwedding@gmail.com"

import random
import helper

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
        self.found_letters = {}
        self.unfound_letters = []
        self.null_letters = []
        self.new_dict = []
        self.new_dict2 = dictionary.copy()

    def AgentFunction(self, percepts):
        """Returns the next word guess given state of the game in percepts

      :param percepts: a tuple of three items: guess_counter, letter_indexes, and letter_states;
               guess_counter is an integer indicating which guess this is, starting with 0 for initial guess;
               letter_indexes is a list of indexes of letters from self.letters corresponding to
                           the previous guess, a list of -1's on guess 0;
               letter_states is a list of the same length as letter_indexes, providing feedback about the
                           previous guess (conveyed through letter indexes) with values of 0 (the corresponding
                           letter was not found in the solution), -1 (the correspond letter is found in the
                           solution, but not in that spot), 1 (the corresponding letter is found in the solution
                           in that spot).
      :return: string - a word from self.dictionary that is the next guess
      """

        # This is how you extract three different parts of percepts.
        guess_counter, letter_indexes, letter_states = percepts

        # Here's where you should put in your code
        print(letter_states)
        if guess_counter == 0:
            self.new_dict2 = self.dictionary.copy()
            self.found_letters.clear()
            self.unfound_letters.clear()
            self.new_dict.clear()

        for x in range(self.word_length):
            if letter_states[x] == 1:
                self.found_letters[x] = self.letters[letter_indexes[x]]
            elif letter_states[x] == 0:
                if self.letters[letter_indexes[x]] not in self.null_letters:
                    self.null_letters.append(self.letters[letter_indexes[x]])
            elif guess_counter == 0:
                pass
            elif letter_states[x] == -1:
                if self.letters[letter_indexes[x]] not in self.unfound_letters:
                    self.unfound_letters.append(self.letters[letter_indexes[x]])

        # Iterating through the dictionary to find the words that contain the correct letters in the wrong places.
        for index in range(len(self.dictionary)):
            # for letter in self.unfound_letters:
            #     if letter not in self.dictionary[index]:
            #         if self.dictionary[index] not in self.new_dict:
            #             self.new_dict.append(self.dictionary[index])

            for letter in self.null_letters:
                if letter in self.dictionary[index]:
                    if self.dictionary[index] not in self.new_dict:
                        self.new_dict.append(self.dictionary[index])

            # and now the letters in the correct places
            for x in range(self.word_length):
                if x in self.found_letters.keys():
                    if self.dictionary[index][x] != self.found_letters[x]:
                        if self.dictionary[index] not in self.new_dict:
                            self.new_dict.append(self.dictionary[index])

        # Iterate through possible words list, checking to see if any of the words contain the correct letters in the
        # correct positions
        print("Length of new_dict: %s" % len(self.new_dict))
        print("Length of new_dict2: %s" % len(self.new_dict2))
        print("Letter States: %s " % letter_states)
        print("Found letters: %s " % self.found_letters)
        print("Unfound letters: %s " % self.unfound_letters)

        for x in range(len(self.new_dict)-1, 0, -1):
            if self.new_dict[x] in self.new_dict2:
                self.new_dict2.remove(self.new_dict[x])

        # guess_index = random.randint(0, (len(self.new_dict2)))
        print("-----------------------")

        # Currently this agent always returns the first word from the dictionary - probably
        # a good idea to replace this with a better guess based on your code above.
        # print(guess_index)
        print(len(self.new_dict2))
        guess = random.choice(self.new_dict2)
        # guess = self.new_dict2[guess_index]

        self.new_dict.clear()
        return guess
