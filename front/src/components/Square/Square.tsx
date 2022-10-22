import React from "react";
import "./SquareStyle.css"

export default function Square({value, onClick, className}: SquareProps) {
    return (
        <button className={"square " + (className)} onClick={onClick}>
            {value}
        </button>
    );
}