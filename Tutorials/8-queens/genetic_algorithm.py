from chess_board import chess_board
import numpy as np
import time

generations = 10
individuals = 10
size = 8
board = chess_board(size)


def make_population(ind):
    for i in range(ind):

        indv = []

        for x in range(size):
            indv.append(np.random.randint(0, size**2))

        indvs.append(indv)
    return indvs


indvs = make_population(individuals)

c_best = None
for i in range(generations):

    for c in indvs:
        f = board.nonattacking_pairs(c)
        print(c, f)
        if c_best is None:
            c_best = c
        elif f > board.nonattacking_pairs(c_best):
            c_best = c

    print(c_best)

    board.show_state(c_best)
    time.sleep(10)

    if board.nonattacking_pairs(c_best) == 28:
        print("Shown board is the solution to the 8-queens problem.")
        time.sleep(999)








for line in indvs:
    print(line)

