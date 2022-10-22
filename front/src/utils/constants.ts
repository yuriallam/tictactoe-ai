const URI = "http://localhost:5000";


const BOARD_CLASSES = [ "show", "show1", "show", "show1", "show2", "show3", "show", "show3", "show" ];
const INITIAL_GAME_PARAMS: InitParamsDto = {
    board_size: 3,
    empty_value: " "
};
const INITIAL_GAME_STATE: GameStatusDto = {
    board: new Array(INITIAL_GAME_PARAMS.board_size ** 2).fill(INITIAL_GAME_PARAMS.empty_value)
};

export {
    URI,
    BOARD_CLASSES,
    INITIAL_GAME_PARAMS,
    INITIAL_GAME_STATE
};