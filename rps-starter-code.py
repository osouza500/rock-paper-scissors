#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

import random

class Player:
    def move(self):
        result = ['rock', 'paper', 'scissors']
        return random.choice(result)

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    pass

class HumanPlayer(Player):
    def move(self):
        result = input('Rock, paper or scissors?\n')
        return result

class ReflectPlayer(Player):
     def learn(self, their_move):
        p1_move = their_move
        return p1_move
           

# class CyclePlayer(Player):
#     pass

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))
            

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2 

    def play_game(self):
        p1_score = 0
        p2_score = 0
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            move1 = self.p1.move()
            move2 = self.p2.move(round, move1) 
            print(f"Player 1: {move1}  Player 2: {move2}")
            if beats(move1, move2) == True:
                p1_score += 1
                print("Player One won.")
                print(f"Score = Player One: {p1_score}, Player Two: {p2_score}.")
            elif beats(move2, move1) == True:
                p2_score += 1
                print("Player Two won.")
                print(f"Score = Player One: {p1_score}, Player Two: {p2_score}.")
            elif move1 == move2:
                print("Tie!")
                print(f"Score = Player One: {p1_score}, Player Two: {p2_score}.")
            self.p1.learn(move1, move2)
            self.p2.learn(move2, move1)    
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()

    # def play_round(self):
    #     move1 = self.p1.move()
    #     move2 = self.p2.move()
    #     print(f"Player 1: {move1}  Player 2: {move2}")
        # self.p1.learn(move1, move2)
        # self.p2.learn(move2, move1)