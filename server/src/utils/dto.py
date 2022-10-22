from abc import ABC, abstractmethod
from typing import List, Optional


class AbstractBaseDto(ABC):
    @abstractmethod
    def to_json(self) -> dict:
        pass

class InitGameDto(AbstractBaseDto):
    def __init__(self, p1: str, p2: str) -> None:
        self.p1 = p1
        self.p2 = p2
        
    def to_json(self) -> dict:
        return {
            "p1": self.p1,
            "p2": self.p2
        }

class InitParamsDto(AbstractBaseDto):
    def __init__(self, board_size: int, empty_value: str) -> None:
        self.board_size = board_size
        self.empty_value = empty_value
        
    def to_json(self) -> dict:
        return {
            "board_size": self.board_size,
            "empty_value": self.empty_value
        }

class MakeMoveDto(AbstractBaseDto):
    def __init__(self, position: int) -> None:
        self.position = position
        
    def to_json(self) -> dict:
        return {
            "position": self.position
        }

class GameStatusDto(AbstractBaseDto):
    def __init__(self, board: List[str], status: str, result: Optional[int], winning_comb: Optional[List[int]], turn: Optional[str], p1: Optional[str], p2: Optional[str]) -> None:
        self.board = board
        self.status = status
        self.result = result
        self.winning_comb = winning_comb
        self.turn = turn
        self.p1 = p1
        self.p2 = p2

    def to_json(self) -> dict:
        return {
            "board": self.board,
            "status": self.status,
            "result": self.result,
            "winning_comb": self.winning_comb,
            "turn": self.turn,
            "p1": self.p1,
            "p2": self.p2
        }