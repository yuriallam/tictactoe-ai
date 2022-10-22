import socketio
from typing import Optional
import time

import utils.helpers as helpers
import utils.enums as enums
import utils.constants as constants
from game.tic_tac_toe import TicTacToe
from players.abstract_player import AbstractPlayer
from players.human_player import HumanPlayer
from utils.dto import InitGameDto, InitParamsDto, MakeMoveDto, GameStatusDto

class GameNamespace(socketio.AsyncNamespace):
    def __init__(self, namespace: Optional[str] = None) -> None:
        super().__init__(namespace)
        self.game: TicTacToe = None
        self.is_playing = False
        self.p_turn: AbstractPlayer = None
        self.status: enums.GameStatus = enums.GameStatus.INITIAL

    async def on_connect(self, sid: str, environ: dict):
        helpers.server_log(sid, "Connected")

        init_params_dto = InitParamsDto(
            constants.BOARD_SIZE,
            enums.BoardValue.EMPTY.value
        )
        await self.emit("init_params", init_params_dto.to_json())

    def on_disconnect(self, sid: str):
        helpers.server_log(sid, "Disconnected")


    async def emit_game_state(self):
        result = None
        winning_comb = None
        winner_response = self.game.check_winner()
        if winner_response is not None:
            result = winner_response["result"]
            winning_comb = winner_response["winning_comb"]

        game_status_dto = GameStatusDto(
            self.game.board.to_json(),
            self.status.value,
            result,
            winning_comb,
            self.game.p_turn.board_value.value,
            self.game.p1.board_value.value,
            self.game.p2.board_value.value
        )
        await self.emit("game_state", game_status_dto.to_json())

    async def on_init_game(self, sid: str, data: dict):
        helpers.server_log(sid, data)

        init_game_params = InitGameDto(**data)
        self.game = TicTacToe(
            helpers.get_player_from_str(init_game_params.p1, enums.BoardValue.X),
            helpers.get_player_from_str(init_game_params.p2, enums.BoardValue.O)
        )
        self.is_playing = False
        self.p_turn = None

        self.status = enums.GameStatus.IN_PROGRESS
        await self.emit_game_state()
        await self.play_game()

    async def on_make_move(self, sid: str, data: dict):
        helpers.server_log(sid, data)

        if self.is_playing:
            return

        make_move_params = MakeMoveDto(**data)
        self.p_turn.next_move = make_move_params.position
        await self.play_game()

    async def play_game(self):
        self.is_playing = True
        while self.game.check_winner() is None:
            self.status = enums.GameStatus.IN_PROGRESS
            await self.emit_game_state()
            self.p_turn = self.game.p_turn
            if isinstance(self.p_turn, HumanPlayer) and self.p_turn.next_move == -1:
                self.status = enums.GameStatus.PENDING
                await self.emit_game_state()
                break
            self.game.make_move()
            self.p_turn.next_move = -1

            if not isinstance(self.game.p1, HumanPlayer) and not isinstance(self.game.p2, HumanPlayer):
                time.sleep(constants.BOT_DELAY)
        else:
            self.status = enums.GameStatus.DONE
            await self.emit_game_state()

        self.is_playing = False