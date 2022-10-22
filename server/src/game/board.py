from typing import List, Optional, Tuple
import utils.constants as constants
import utils.enums as enums


class Board:
    def __init__(self, size = constants.BOARD_SIZE) -> None:
        self.size = size
        self.values = [ enums.BoardValue.EMPTY for _ in range(size**2) ]
        self.winning_combinations = self.__get_winning_combinations()
    
    def __str__(self) -> str:
        lines = [
            f"|".join([self.values[j].value for j in range(i, i+self.size)]) for i in range(0, self.size**2, self.size)
        ]

        return "\n".join(lines)

    def is_full(self) -> bool:
        return enums.BoardValue.EMPTY not in self.values

    def empty_values(self) -> int:
        return self.values.count(enums.BoardValue.EMPTY)

    def get_winner(self) -> Optional[dict]:
        player_values = [ enums.BoardValue.O, enums.BoardValue.X ]
        for player_value in player_values:
            winning_comb = self.__is_winner(player_value)
            if winning_comb is not None:
                return { "player_value": player_value, "winning_comb": winning_comb }
    
    def place_value(self, position: int, board_value: enums.BoardValue) -> bool:
        if board_value == enums.BoardValue.EMPTY:
            return False

        if position < 0 or position >= self.size**2:
            return False
        
        if self.values[position] != enums.BoardValue.EMPTY:
            return False
        
        self.values[position] = board_value
        return True

    def __is_winner(self, board_value: enums.BoardValue) -> Optional[List[int]]:
        for winning_combination in self.winning_combinations:
            winner = True
            for index in winning_combination:
                if self.values[index] != board_value:
                    winner = False
                    break
            if winner:
                return winning_combination

    def __get_winning_combinations(self) -> List[List[int]]:
        result = []

        # Horizontal
        for i in range(0, self.size**2, self.size):
            result.append([
                j for j in range(i, i+self.size)
            ])

        # Vertical
        for i in range(self.size):
            result.append([
                i + (self.size * j) for j in range(self.size)
            ])

        # Left Diagonal
        result.append([
            i + (self.size * i) for i in range(self.size)
        ])

        # Right Diagonal
        result.append([
            (i + 1) * (self.size - 1) for i in range(self.size)
        ])

        return result

    def to_json(self):
        return [ board_value.value for board_value in self.values ]