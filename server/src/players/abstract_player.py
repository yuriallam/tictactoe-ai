from abc import ABC, abstractmethod
from game.board import Board
import utils.enums as enums


class AbstractPlayer(ABC):
    def __init__(self, board_value: enums.BoardValue):
        self.board_value = board_value
        self.next_move = -1

    @abstractmethod
    def get_next_move(self, board: Board) -> int:
        pass