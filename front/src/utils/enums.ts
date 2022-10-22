enum Events {
    INIT_PARAMS = "init_params",
    GAME_STATE = "game_state"
};

enum GameStatus {
    INITIAL = "INITIAL",
    IN_PROGRESS = "IN_PROGRESS",
    PENDING = "PENDING",
    DONE = "DONE"
};

export {
    Events,
    GameStatus
};