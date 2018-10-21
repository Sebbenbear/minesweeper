package minesweeper.model;

import minesweeper.model.Cell;

class Board {

    Cell[][] board;

    Board(int width, int height) {
        this.board = new Cell[width][height];
    }
}