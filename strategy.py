"""Provides different door choosing strategies."""

import numpy as np

class ChooseDoor:
    @staticmethod
    def first_choice(n):
        raise NotImplementedError

    @staticmethod
    def second_choice(n, closed, first_guess):
        raise NotImplementedError

class RandomDoorNoChange(ChooseDoor):
    @staticmethod
    def first_choice(n):
        return np.random.randint(n)

    @staticmethod
    def second_choice(n, closed, first_guess):
        return first_guess

class RandomDoor(ChooseDoor):
    @staticmethod
    def first_choice(n):
        return np.random.randint(n)

    @staticmethod
    def second_choice(n, closed, first_guess):
        return np.random.choice(list(closed))

class NewRandomDoor(ChooseDoor):
    @staticmethod
    def first_choice(n):
        return np.random.randint(n)

    @staticmethod
    def second_choice(n, closed, first_guess):
        closed = closed.copy()
        closed.remove(first_guess)
        return np.random.choice(list(closed))
