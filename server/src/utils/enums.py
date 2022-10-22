import enum


class BoardValue(enum.Enum):
    EMPTY = " "
    X = "X"
    O = "O"

class GameStatus(enum.Enum):
    INITIAL = "INITIAL"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING = "PENDING"
    DONE = "DONE"