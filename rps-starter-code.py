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


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    # Inicializador; (objeto criado, instância da classe Player, instância da classe 
    # Player, argumentos passados em game = Game(Player(), Player()). 
    def __init__(self, p1, p2):
    # Instância game ponto classe Player = p1;
    # Instância game ponto classe Player = p2;
        self.p1 = p1
        self.p2 = p2

    def score(self, p1, p2):
        p1_score = 0
        p2_score = 0
        

    def play_round(self):
    # move1 = instância da classe Player chama o método move;
    # o resultado é armazenado na variável
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()
