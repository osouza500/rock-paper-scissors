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
    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            print_pause("Rock, paper or scissors?")
            player_move = input().lower()
            if player_move not in moves:
                print_pause("Type a valid input.")
            else:
                return player_move


class ReflectPlayer(Player):
    previous_move = ""

    def move(self, round):
        if round == 0:
            return random.choice(moves)
        else:
            return ReflectPlayer.previous_move

    def learn(self, their_move):
        ReflectPlayer.previous_move = their_move


class CyclePlayer(Player):
    first_move = ""
    moves = ["rock", "paper", "scissors"]

    def move(self, round):
        if round == 0:
            return random.choice(CyclePlayer.moves)
        if round == 1:
            CyclePlayer.moves.remove(CyclePlayer.first_move)
            if round % 3 == 1:
                return CyclePlayer.moves[0]
            elif round % 3 == 2:
                return CyclePlayer.moves[1]
        if round > 1:
            if round % 3 == 0:
                return CyclePlayer.first_move
            elif round % 3 == 1:
                return CyclePlayer.moves[0]
            elif round % 3 == 2:
                return CyclePlayer.moves[1]

    def learn(self, my_move):
        CyclePlayer.first_move = my_move


class Game:
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self, round):
        strategies = (
                     Player.move(self),
                     RandomPlayer.move(self),
                     ReflectPlayer.move(self, round),
                     CyclePlayer.move(self, round)
                     )
        move1 = HumanPlayer.move(self)
        # move2 = CyclePlayer.move(self, round)
        move2 = random.choice(strategies)
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
        if round == 2:
            print_pause(f"Final score: Player One {self.p1_score}, "
                        f"Player Two {self.p2_score}.")
            if self.p1_score > self.p2_score:
                print_pause("Victory for Player One!")
            elif self.p2_score > self.p1_score:
                print_pause("Victory for Player Two!")
            else:
                print_pause("Tie!")
        ReflectPlayer.learn(self, move1)
        if round == 0:
            CyclePlayer.learn(self, move2)

    def play_game(self):
        self.rounds = 3
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
