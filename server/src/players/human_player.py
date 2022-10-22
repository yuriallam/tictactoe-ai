from players.abstract_player import AbstractPlayer
from game.board import Board
import utils.enums as enums


class HumanPlayer(AbstractPlayer):
    def __init__(self, board_value: enums.BoardValue):
        super().__init__(board_value)

    def get_next_move(self, board: Board) -> int:
        return self.next_move