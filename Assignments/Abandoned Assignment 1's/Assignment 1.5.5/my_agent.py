__author__ = "Kurt Wedding-Speight"
__organization__ = "COSC343/AIML402, University of Otago"
__email__ = "wedku875@student.otago.ac.nz"


import numpy as np
import helper as h


class WordleAgent():
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
        self.DICT = dictionary
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
      :return: string - a word from self.dictionary that is the next guess
      """

        # This is how you extract three different parts of percepts.
        guess_counter, letter_indexes, letter_states = percepts

        # Here's where you should put in your code
        if guess_counter == 0:
            self.dictionary = self.DICT
        
        strBuilder = np.full(self.word_length, -1)
        nullLetters = []
        possLetters = []

        # Creating the arrays for the letters that are not found and the letters that are found, and where found
        # letters are.
        for x in range(self.word_length): # For each letter in the word/guess
            if letter_states[x] == 1: # If the letter was in the correct place
                strBuilder[x] = letter_indexes[x] # Add the letter to the stringBuilder in the correct place
            elif letter_states[x] == 0: # If the letter was not in the answer
                nullLetters.append(letter_indexes[x]) # add it to a list of incorrect letters
            else: # If the letter was in the answer but not in the correct place
                if letter_indexes[x] in nullLetters:
                    nullLetters.remove(letter_indexes[x]) # this is incase the possible letter is already in the null list
                possLetters.append(letter_indexes[x]) # add it to a list of possible letters

        for elem in strBuilder:
            if elem == -1: # if the element is empty
                if len(possLetters) == 0: # and there are no more possible letters
                    strBuilder[elem] = np.random.randint(0, len(self.letters) - 1) # pick a random letter
                elif len(possLetters) != 0:
                    #
                    pass

        for letter in nullLetters:
            for num in range(len(self.dictionary)-1, 0, -1):
                if self.letters[letter] in self.dictionary[num-1]:
                    self.dictionary.pop(num-1)

        # Currently this agent always returns the first word from the dictionary - probably
        # a good idea to replace this with a better guess based on your code above.
        return self.dictionary[np.random.randint(0, len(self.dictionary))]

        # answer = ""
        # for element in strBuilder:
        #     answer += element
        # return answer
