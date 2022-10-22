import random
from typing import Optional
from players.abstract_player import AbstractPlayer
from game.board import Board


class TicTacToe:
    def __init__(self, p1: AbstractPlayer, p2: AbstractPlayer) -> None:
        self.board = Board()
        self.p1 = p1
        self.p2 = p2
        self.p_turn = random.choice([p1 , p2])

    def make_move(self) -> None:
        position = self.p_turn.get_next_move(self.board)
        while not self.board.place_value(position, self.p_turn.board_value):
            print("Position invalid!")
            position = self.p_turn.get_next_move(self.board)        
        
        self.p_turn = self.p2 if self.p_turn == self.p1 else self.p1

    def check_winner(self) -> Optional[dict]:
        winner_response = self.board.get_winner()
        result = None
        if winner_response is not None:
            if winner_response["player_value"] == self.p1.board_value:
                result = 1

            if winner_response["player_value"] == self.p2.board_value:
                result = 2
        elif self.board.is_full():
            result = 0

        if result is not None:
            return {
                "result": result,
                "winning_comb": None if winner_response is None else winner_response["winning_comb"]
            }