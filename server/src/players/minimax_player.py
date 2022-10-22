import math
from players.abstract_player import AbstractPlayer
from game.board import Board
import utils.enums as enums


class MinimaxPlayer(AbstractPlayer):
    def __init__(self, board_value: enums.BoardValue):
        super().__init__(board_value)
        self.other_board_value = enums.BoardValue.X if self.board_value == enums.BoardValue.O else enums.BoardValue.O 

    def get_next_move(self, board: Board) -> int:
        best_score = -math.inf
        best_move = 0
        for i in range(len(board.values)):
            if board.values[i] == enums.BoardValue.EMPTY:
                board.values[i] = self.board_value
                score = self.__minimax(board, 0, False, -math.inf, math.inf)
                board.values[i] = enums.BoardValue.EMPTY
                
                if score > best_score:
                    best_score = score
                    best_move = i

        return best_move

    def __minimax(self, board: Board, depth: int, is_maximising: bool, alpha: float, beta: float) -> int:
        winner_response = board.get_winner()
        if winner_response is not None:
            if winner_response["player_value"] == self.board_value:
                return 1

            if winner_response["player_value"] == self.other_board_value:
                return -1
        
        if board.is_full():
            return 0

        best_score = -math.inf if is_maximising else math.inf
        for i in range(len(board.values)):
            if board.values[i] == enums.BoardValue.EMPTY:
                board.values[i] = self.board_value if is_maximising else self.other_board_value 
                score = self.__minimax(board, depth + 1, not is_maximising, alpha, beta)
                board.values[i] = enums.BoardValue.EMPTY
                best_score = max(score, best_score) if is_maximising else min(score, best_score)

                # Alpha beta pruning
                if is_maximising:
                    alpha = max(alpha, best_score)
                else:
                    beta = min(beta, best_score)
                
                if beta <= alpha:
                    break

        return best_score
