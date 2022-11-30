import random
import time

moves = ["rock", "paper", "scissors"]


def print_pause(message):
    time.sleep(.5)
    print(message)


def continue_quit():
    print_pause("Play again? Y/N.")
    answer = input().lower()
    if answer == "y":
        game.play_game()
    elif answer == "n":
        print_pause("Good bye!")
        quit()
    else:
        print_pause("Type a valid input.\n")
        continue_quit()


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Player:
    index = 0
    check = True
    my_move = random.choice(moves)
    their_move = random.choice(moves)

    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass

class AllRockPlayer(Player):
    pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, paper or scissors?").lower()
            if move in moves:
                return move
            print(f"The move {move} is invalid. Try")


class ReflectPlayer(Player):
    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        previous_move = self.my_move
        if self.check is True:
            self.check = False
            self.index += 1
            return self.their_move
        if self.index % len(moves) == 0:
            self.index += 1
            return previous_move
        elif self.index % len(moves) == 1 and previous_move != moves[1]:
            self.index += 1
            return moves[1]
        elif self.index % len(moves) == 2 and previous_move != moves[2]:
            self.index += 1
            return moves[2]
        else:
            self.index += 1
            return moves[0]

    def learn(self, my_move, their_move):
        self.my_move = my_move


class Game:
    check = True
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self, round):
        # strategies = (
        #              Player.move(self),
        #              RandomPlayer.move(self),
        #              ReflectPlayer.move(self),
        #              CyclePlayer.move(self)
        #              )
        move1 = HumanPlayer.move(self)
        move2 = CyclePlayer.move(self)
        # move2 = random.choice(strategies)
        print_pause(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) is True:
            self.p1_score += 1
            print_pause("Player One won.")
            print(f"Score = Player One: {self.p1_score}, "
                  f"Player Two: {self.p2_score}.\n")
        elif beats(move2, move1) is True:
            self.p2_score += 1
            print_pause("Player Two won.")
            print(f"Score = Player One: {self.p1_score}, "
                  f"Player Two: {self.p2_score}.\n")
        elif move1 == move2:
            print_pause("Tie!")
            print(f"Score = Player One: {self.p1_score}, "
                  f"Player Two: {self.p2_score}.\n")
        if round == 5:
            print_pause(f"Final score: Player One {self.p1_score}, "
                        f"Player Two {self.p2_score}.")
            if self.p1_score > self.p2_score:
                print_pause("Victory for Player One!")
            elif self.p2_score > self.p1_score:
                print_pause("Victory for Player Two!")
            else:
                print_pause("Tie!")
        ReflectPlayer.learn(self, move1, move2)
        if self.check is True:
            self.check = False
            CyclePlayer.learn(self, move1, move2)

    def play_game(self):
        self.rounds = 6
        self.p1_score = 0
        self.p2_score = 0
        print_pause("Game start!\n")
        for round in range(self.rounds):
            print_pause(f"Round {round}:")
            self.play_round(round)
        print_pause("Game over!")
        continue_quit()


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
