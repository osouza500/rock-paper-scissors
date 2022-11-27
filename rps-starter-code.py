import random
import time


def print_pause(message):
    time.sleep(1)
    print(message)


def continue_quit():
    print_pause("Play again? Y/N.")
    answer = input().lower()
    if answer == "y" or "yes":
        game.play_game()
    elif answer == "n" or "no":
        print_pause("Good bye!")
        quit()
    else:
        print_pause("Type a valid input.")
        continue_quit()


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


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


class Game:
    # store scores and both human and machine 
    # previous moves
    p1_score = 0
    p2_score = 0
    previous_move = ""


    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    def play_round(self, round):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if round > 0 and type(self.p2) != RandomPlayer:
            move2 = self.previous_move
        print_pause(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) is True:
            self.p1_score += 1
            print_pause("Player One won.")
            print(f"Score = Player One: {self.p1_score}, "
                  f"Player Two: {self.p2_score}.")
        elif beats(move2, move1) is True:
            self.p2_score += 1
            print_pause("Player Two won.")
            print(f"Score = Player One: {self.p1_score}, "
                  f"Player Two: {self.p2_score}.")
        elif move1 == move2:
            print_pause("Tie!")
            print(f"Score = Player One: {self.p1_score}, "
                  f"Player Two: {self.p2_score}.")
        if round == 2:
            print_pause(f"Final score: Player One {self.p1_score}, "
                        f"Player Two {self.p2_score}.")
            if self.p1_score > self.p2_score:
                print_pause("Victory for Player One!")
            elif self.p2_score > self.p2_score:
                print_pause("Victory for Player Two!")
            else:
                print_pause("Tie!")
        # assign human or machine previous move (accordingly to the 
        # opponent subclass) to previous_move class variable
        self.previous_move = self.p2.learn(move2, move1)


    def play_game(self):
    # restart score everytime game.play_game()
    # is called
        self.p1_score = 0
        self.p2_score = 0
        print_pause("Game start!")
        for round in range(3):
            print_pause(f"Round {round}:")
            self.play_round(round)
        print_pause("Game over!")
        continue_quit()


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
