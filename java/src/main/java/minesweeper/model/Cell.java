package minesweeper.model;

class Cell {
    private final boolean hasMine;
    private final int mineCount;

    private boolean isVisible;
    private boolean hasFlag;

    private Cell(boolean hasMine, int mineCount) {
        this.hasMine = hasMine;
        this.mineCount = mineCount;
    }

    static Cell createMine() {
        return new Cell(/* hasMine= */ true, /* mineCount= */ 0);
    }

    static Cell createMineCount(int mineCount) {
        return new Cell(/* hasMine= */ false, mineCount);
    }

    boolean isVisible() {
        return isVisible;
    }

    void makeVisible() {
        isVisible = true;
    }

    boolean hasFlag() {
        return hasFlag;
    }

    void setHasFlag(boolean hasFlag) {
        this.hasFlag = hasFlag;
    }
}