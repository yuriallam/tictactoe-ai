import utils.enums as enums
from players.abstract_player import AbstractPlayer
from players.human_player import HumanPlayer
from players.minimax_player import MinimaxPlayer
from players.expectimax_player import ExpectimaxPlayer
from datetime import datetime


def get_player_from_str(p: str, board_value: enums.BoardValue) -> AbstractPlayer:
    if p.lower() == "human":
        return HumanPlayer(board_value)
    elif p.lower() == "minimax":
        return MinimaxPlayer(board_value)
    elif p.lower() == "expectimax":
        return ExpectimaxPlayer(board_value)

def server_log(sid: str, message: str):
    print(datetime.now(), ": ", sid, " => ", message, sep="")