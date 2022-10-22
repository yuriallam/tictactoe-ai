import math
from players.abstract_player import AbstractPlayer
from game.board import Board
import utils.enums as enums


class ExpectimaxPlayer(AbstractPlayer):
    def __init__(self, board_value: enums.BoardValue):
        super().__init__(board_value)
        self.other_board_value = enums.BoardValue.X if self.board_value == enums.BoardValue.O else enums.BoardValue.O 

    def get_next_move(self, board: Board) -> int:
        best_score = -math.inf
        best_move = 0
        for i in range(len(board.values)):
            if board.values[i] == enums.BoardValue.EMPTY:
                board.values[i] = self.board_value
                score = self.__expectimax(board, 0, True)
                board.values[i] = enums.BoardValue.EMPTY
                
                if score > best_score:
                    best_score = score
                    best_move = i

        return best_move

    def __expectimax(self, board: Board, depth: int, is_expecting: bool) -> int:
        winner_response = board.get_winner()
        if winner_response is not None:
            if winner_response["player_value"] == self.board_value:
                return 1

            if winner_response["player_value"] == self.other_board_value:
                return -1
        
        if board.is_full():
            return 0

        calculated_score = 0 if is_expecting else -math.inf
        for i in range(len(board.values)):
            if board.values[i] == enums.BoardValue.EMPTY:
                board_empty_values = board.empty_values()
                board.values[i] = self.other_board_value if is_expecting else self.board_value
                score = self.__expectimax(board, depth + 1, not is_expecting)
                board.values[i] = enums.BoardValue.EMPTY

                if is_expecting:
                    calculated_score += (1/board_empty_values) * score
                else:
                    calculated_score = max(score, calculated_score)

        return calculated_score
