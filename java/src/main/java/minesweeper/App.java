package minesweeper;

import minesweeper.controller.GameController;

public class App {
    public static void main( String[] args ) {
        System.out.println( "Starting game..." );
        new GameController().mainLoop();
    }
}
