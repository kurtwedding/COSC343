__author__ = "Kurt Wedding-Speight"
__organization__ = "COSC343/AIML402, University of Otago"
__email__ = "wedku875@student.otago.ac.nz"

import numpy as np
import time

agentName = "Kurt's Agent"
perceptFieldOfVision = 3   # Choose either 3,5,7 or 9
perceptFrames = 1          # Choose either 1,2,3 or 4
trainingSchedule = [("self", 100), ("random", 50)]

# This is the class for your snake/agent
class Snake:

    def __init__(self, nPercepts, actions):
        # You should initialise self.chromosome member variable here (whatever you choose it
        # to be - a list/vector/matrix of numbers - and initialise it with some random
        # values)
        self.chromosome = np.random.uniform(-20, 20, (3, nPercepts+1))
        # print(self.chromosome)

        # self.chromosome = np.random.uniform(-1, 1, (nPercepts, 3))
        self.nPercepts = nPercepts
        self.actions = actions



    def AgentFunction(self, percepts):

        # percepts = percepts.flatten()
        # print(percepts[0])
        percepts = percepts[0]
        flatPercepts = percepts.flatten()
        for i in range(len(flatPercepts)):
            if flatPercepts[i] == 2:
                flatPercepts[i] = 20 # Make the food more attractive
            elif flatPercepts[i] == 1:
                flatPercepts[i] = -20 # Make the friendlies less attractive
            elif flatPercepts[i] == -1:
                flatPercepts[i] = -20 # Make the enemies less attractive
        # print(flatPercepts)

        # Implementing the a1 = w1p1 + w2p2 + ... + w9p9 + w10 algorithm to find action weights
        action = np.zeros(3)
        for x, arr in enumerate(self.chromosome):
            for i in range(len(arr)):
                if i == len(arr)-1:
                    action[x] += arr[i]
                else:
                    action[x] += arr[i] * flatPercepts[i]
        
        # print(action)
        
        #
        # The index of the largest numbers in the 'actions' vector/list is the action taken
        # with the following interpretation:
        # 0 - move left
        # 1 - move forward
        # 2 - move right
        #
        #
        # Different 'percepts' values should lead to different 'actions'.  This way the agent
        # reacts differently to different situations.
        #
        # Different 'self.chromosome' should lead to different 'actions'.  This way different
        # agents can exhibit different behaviour.

        # .

        return np.argmax(action) -1 # Return the index of the action with the highest weight

        # index = np.random.randint(low=0, high=len(self.actions))
        # return self.actions[index]

def evalFitness(population):

    N = len(population)

    # Fitness initialiser for all agents
    fitness = np.zeros((N))

    # This loop iterates over your agents in the old population - the purpose of this boiler plate
    # code is to demonstrate how to fetch information from the old_population in order
    # to score fitness of each agent
    for n, snake in enumerate(population):
        # snake is an instance of Snake class that you implemented above, therefore you can access any attributes
        # (such as 'self.chromosome').  Additionally, the object has the following attributes provided by the
        # game engine:
        #       snake.size - list of snake sizes over the game turns

        maxSize = np.max(snake.sizes)
        turnsAlive = np.sum(snake.sizes > 0)
        maxTurns = len(snake.sizes)

        # This fitness functions considers snake size plus the fraction of turns the snake
        # lasted for.  It should be a reasonable fitness function, though you're free
        # to augment it with information from other stats as well

        # In testing, the turnsAlive was not a good indicator of fitness, as snakes can loop 
        # around themselves forever if they are 4 long, and this skews the turnsAlive causing
        # snakes that do not progress to be considered fitter than other snakes, so I have
        # altered it so it has less impact.
        fitness[n] = maxSize + turnsAlive / (2*maxTurns)


    return fitness

def newGeneration(old_population):

    # This function should return a tuple consisting of:
    # - a list of the new_population of snakes that is of the same length as the old_population,
    # - the average fitness of the old population

    N = len(old_population)

    nPercepts = old_population[0].nPercepts
    actions = old_population[0].actions

    fitness = evalFitness(old_population)

    # At this point you should sort the old_population snakes according to fitness, setting it up for parent
    # selection.
    values = list()

    for i in range(N):
        values.append((fitness[i], old_population[i].chromosome.tolist()))
    values.sort(key=lambda x: x[0], reverse=True) # sort the list of chromosomes by fitness, descending
    old_population = values

    # Create new population list...
    new_population = list()
    for n in range(N):

        # Create a new snake
        new_snake = Snake(nPercepts, actions)

        # Here you should modify the new snakes chromosome by selecting two parents (based on their
        # fitness) and crossing their chromosome to overwrite new_snake.chromosome

        # Consider implementing elitism, mutation and various other
        # strategies for producing a new creature.

        # ====== Elitism =======
        parent1 = old_population[0][1] # returns an array of chromosomes
        parent2 = old_population[1][1] # returns an array of chromosomes
        for a in range(len(parent1)):
            for n in range(len(parent1[a])):
                r = np.random.uniform(0, 1)
                if r < 0.04: # Mutation has a 4% chance of happening
                    pass # the initialization already randomizes the chromosome
                elif r < 0.52:
                    new_snake.chromosome[a][n] = parent1[a][n]
                else:
                    new_snake.chromosome[a][n] = parent2[a][n]        

        # Add the new snake to the new population
        new_population.append(new_snake)

    # At the end you need to compute the average fitness and return it along with your new population
    avg_fitness = np.mean(fitness)

    return (new_population, avg_fitness)
