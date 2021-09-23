import random
import math

class Player:
    def __init__(self, letter):
        self.__letter = letter # letter is x or o

    @property
    def letter(self):
        return self.__letter

    # get next move in the game
    def get_next_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_next_move(self, game):        
        while True:
            square = int(input(f"{self.letter}'s turn. Input move (0-{game.size**2 - 1}): "))

            try:
                if square not in game.get_available_moves():
                    raise ValueError
                return square
            except ValueError:
                print("Invalid square. Try again.")


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_next_move(self, game):
        square = random.choice(game.get_available_moves())
        return square


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_next_move(self, game):
        if len(game.get_available_moves()) == game.size ** 2:
            square = random.choice(game.get_available_moves())
        else:
            # get the square based on the minimax algorithm
            square = self.minimax(game, self.letter)["position"]

        return square

    def minimax(self, state, cur_player):
        myself = self.letter
        other_player = "O" if cur_player == "X" else "X"

        # base case
        if state.cur_winner == other_player:
            intercept = 1 if other_player == myself else -1            
            return { "position": None, "score": intercept * (state.get_num_empty_squares() + 1) }
        # if no empty square
        elif not state.has_empty_squares():
            return { "position": None, "score": 0 }

        # init a dict to save best pos and score
        intercept = -1 if cur_player == myself else 1
        best = { "position": None, "score": intercept * math.inf }

        for possible_move in state.get_available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, cur_player)
            
            # step 2: recursively simulate a game after making a move using minimax
            sim_score = self.minimax(state, other_player)
            
            # step 3: undo the move
            state.board[possible_move] = " "
            state.cur_winner = None
            sim_score["position"] = possible_move
            
            # step 4: update the dict if necessary
            if cur_player == myself:
                if sim_score["score"] > best["score"]:
                    best = sim_score
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score

        return best
