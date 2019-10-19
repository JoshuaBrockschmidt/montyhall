# Experimentally Demonstrating the Monty Hall Problem

## Problem Statement

Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

## Problem Implementation

We will start with a hall with `n` closed doors. The player will then select a door. Then `m < n-1` of the other doors will be opened. The player will then be allowed to change their guess to one of the remaining doors. Success will be measured by whether the player selects the door with the car behind it.

## Strategies

We will test the probabilities of success for the following strategies,

1) Choose a random door and maintain that choice.
2) Choose a random door and then randomly select a second door.
3) Choose a random door and then randomly select a second door excluding the original selection.
