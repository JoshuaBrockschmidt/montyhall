#!/usr/bin/python3

import csv
import numpy as np

import strategy

# Range of n values to test on.
N_RANGE = (3, 1001)

# Number of trials to run for each value of n.
NUM_TRIALS = 10000

STRATS = [strategy.RandomDoorNoChange, strategy.RandomDoor, strategy.NewRandomDoor]

if __name__ == '__main__':
    print('Calculating probabilities...')
    m = 1
    for n in range(*N_RANGE):
        print('\nn={}'.format(n))
        for i, strat in enumerate(STRATS):
            successes = 0
            for _ in range(NUM_TRIALS):
                correct = np.random.randint(0, n)
                choice1 = strat.first_choice(n)
                choose_from = list(range(0, n))
                choose_from.remove(choice1)
                if choice1 != correct:
                    choose_from.remove(correct)
                closed = list(np.random.permutation(choose_from)[m:])
                for j in list({choice1, correct}):
                    closed.append(j)
                assert len(closed) == n - m
                choice2 = strat.second_choice(n, closed, choice1)
                if choice2 == correct:
                    successes += 1
            prob = successes / NUM_TRIALS
            print('    ({}):\t{}'.format(i, prob))
