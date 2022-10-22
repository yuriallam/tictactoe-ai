import React, { useEffect, useState } from "react";
import "./GameScreenStyle.css";
import Square from "../../components/Square";
import { FiRotateCcw } from "react-icons/fi"
import { io, Socket } from "socket.io-client";
import {
    URI,
    BOARD_CLASSES,
    INITIAL_GAME_PARAMS,
    INITIAL_GAME_STATE
} from "../../utils/constants";
import { Events, GameStatus } from "../../utils/enums";


let socket: Socket;
export default function GameScreen() {
    const [gameParams, setGameParams] = useState(INITIAL_GAME_PARAMS);
    const [gameState, setGameState] = useState(INITIAL_GAME_STATE);
    const [player1, setPlayer1] = useState<Player>(null);
    const [player2, setPlayer2] = useState<Player>(null);

    useEffect(() => {
        socket = io(URI);
        socket.on(Events.GAME_STATE, (data: GameStatusDto) => {
            setGameState(data);
        });
        
        socket.on(Events.INIT_PARAMS, (data: InitParamsDto) => {
            setGameParams(data);
        });

        return () => {
            socket.close();
            return;
        }
    }, []);

    useEffect(() => {
        if (player1 !== null && player2 !== null) {
            socket.emit("init_game", { p1: player1, p2: player2 });
        }
    }, [player1, player2]);

    const handleClick = (index: number) => {
        if (gameState.status !== GameStatus.PENDING || gameState.board[index] !== gameParams.empty_value) return;
        socket.emit("make_move", { position: index });
    };

    const handleRetry = () => {
        setPlayer1(null);
        setPlayer2(null);
    };

    const getHeaderText = () => {
        let headerText = "";
        if (player1 === null || player2 === null) headerText = "Select Players";
        else if (gameState.status === GameStatus.DONE) {
            if (gameState.result === 0) headerText = "Draw";
            else if (gameState.result === 1) headerText = "Player 1 won";
            else if (gameState.result === 2) headerText = "Player 2 won";
        }
        else if (gameState.turn === "X") headerText = "Player 1 to play";
        else if (gameState.turn === "O") headerText = "Player 2 to play";
        return headerText;
    };

    const getSquareColorClass = (index: number) => {
        if (gameState.winning_comb != null && gameState.winning_comb.includes(index)) {
            return "square-red";
        }
        return "square-aqua";
    };

    const disable = (player1 && player2)? " disable" : "";

    return (
        <div className="main">
            <div className="player1">
                <h1>Player 1 (X)</h1>
                <button className={"playerButton" + (player1 === "Human" ? " selected" : "") + (disable)}onClick={() => setPlayer1("Human")} >Human</button>
                <button className={"playerButton" + (player1 === "Minimax" ? " selected" : "") + (disable)}onClick={() => setPlayer1("Minimax")}>Minimax</button>
                <button className={"playerButton" + (player1 === "Expectimax" ? " selected" : "") + (disable)}onClick={() => setPlayer1("Expectimax")}>Expectimax</button>
                <h2>{player1}</h2>
            </div>
            <div className="board">
                <p className="header-text">{getHeaderText()}</p>
                {player1 && player2 && <div className="game" >
                    {gameState.board.map((value, index) => (
                        <Square key={index} className={`${BOARD_CLASSES[index]}  ${getSquareColorClass(index)}`}  onClick={() => handleClick(index)} value={value} />
                    ))}
                </div>}

            <button className="retry" onClick={handleRetry} ><FiRotateCcw size={50} /></button>
            </div>
            <div className="player1">
                <h1>Player 2 (O)</h1>
                <button className={"playerButton" + (player2 === "Human" ? " selected" : "") + (disable)}onClick={() => setPlayer2("Human")}>Human</button>
                <button className={"playerButton" + (player2 === "Minimax" ? " selected" : "") + (disable)}onClick={() => setPlayer2("Minimax")}>Minimax</button>
                <button className={"playerButton" + (player2 === "Expectimax" ? " selected" : "") + (disable)}onClick={() => setPlayer2("Expectimax")}>Expectimax</button>
                <h2>{player2}</h2>
            </div>
        </div>
    );
}