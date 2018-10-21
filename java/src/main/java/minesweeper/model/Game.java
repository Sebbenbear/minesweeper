package minesweeper.model;

import minesweeper.model.Board;

public class Game {

    private Board board;

    public Game() {
        System.out.println("I made a game");
        Board board = new Board(10, 20);
    }
}
