import random
import time

moves = ["rock", "paper", "scissors"]


def print_pause(message):
    time.sleep(0)
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
    p1_previous_move = ""

    def learn(self, my_move, their_move):
        ReflectPlayer.p1_previous_move = their_move


class CyclePlayer(Player):
    p2_previous_move = ""

    def move(self, round):
        
        if round == 0:
            return random.choice(moves)
        elif round > 0:
            iv_moves = ['rock', 'paper', 'scissors']
            if CyclePlayer.p2_previous_move in iv_moves:
                iv_moves.remove(CyclePlayer.p2_previous_move)
                return random.choice(iv_moves)

    def learn(self, my_move, their_move):
        CyclePlayer.p2_previous_move = my_move


class Game:
    p1_score = 0
    p2_score = 0
    previous_move = ""

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self, round):
        move1 = HumanPlayer.move(self)
        move2 = CyclePlayer.move(self, round)
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
            elif self.p2_score > self.p2_score:
                print_pause("Victory for Player Two!")
            else:
                print_pause("Tie!")
        CyclePlayer.learn(self, move1, move2)        

        

    def play_game(self):
        self.p1_score = 0
        self.p2_score = 0
        print_pause("Game start!\n")
        for round in range(3):
            print_pause(f"Round {round}:")
            self.play_round(round)
        print_pause("Game over!")
        continue_quit()


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()

# if round > 0 and type(self.p2) != RandomPlayer:
        #     move2 = self.previous_move
        # self.previous_move = self.p2.learn(move2, move1)