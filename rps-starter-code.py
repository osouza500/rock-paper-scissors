import random
import time

def print_pause(message):
    time.sleep(1)
    print(message)


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
        result = ['rock', 'paper', 'scissors']
        while True:
            print_pause("Rock, paper or scissors?")
            player_move = input().lower()
            if player_move not in result:
                print_pause("Type a valid input.")
            else:
                return player_move 


class ReflectPlayer(Player):
    def learn(self, my_move, their_move):
        p1_move = their_move
        return p1_move


class CyclePlayer(Player):
    def learn(self, my_move, their_move):
        result = ['rock', 'paper', 'scissors']
        if my_move in result:
            result.remove(my_move)
            return random.choice(result)


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
        print_pause("Game start!")
        for round in range(3):
            print_pause(f"Round {round}:")
            move1 = self.p1.move()
            if round == 0:
                move2 = self.p2.move()
            print_pause(f"Player 1: {move1}  Player 2: {move2}")
            if beats(move1, move2) is True:
                p1_score += 1
                print_pause("Player One won.")
                print_pause(f"Score = Player One: {p1_score}, "
                            f"Player Two: {p2_score}.")
            elif beats(move2, move1) is True:
                p2_score += 1
                print_pause("Player Two won.")
                print_pause(f"Score = Player One: {p1_score}, "
                            f"Player Two: {p2_score}.")
            elif move1 == move2:
                print_pause("Tie!")
                print_pause(f"Score = Player One: {p1_score}, "
                            f"Player Two: {p2_score}.")
            move2 = self.p2.learn(move2, move1)
        print_pause("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()

    # def play_round(self, p1_score, p2_score):
    #     move1 = self.p1.move()
    #     move2 = self.p2.move()
    #     print(f"Player 1: {move1}  Player 2: {move2}")
    #     self.p1.learn(move1, move2)
    #     self.p2.learn(move2, move1)
