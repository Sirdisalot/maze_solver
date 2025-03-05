from cell import Cell
import time
import random

class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win,
                 seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cell = []

        self._create_cell()


    def _create_cell(self):
        for i in range(self._num_cols): # Build columns
            column = []
            for j in range(self._num_rows): # Add _cell to column
                column.append(Cell(self._win))
            self._cell.append(column)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return  # don't draw if we don't have a window
        # calculate cell coordinates based on grid position
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cell[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is not None:
            self._win.redraw()
            time.sleep(0.03)

    def _break_entrance_and_exit(self):
        # break entance at top of top-left cell
        self._cell[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        # break exit at bottom of bottom-right cell
        self._cell[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cell[i][j].visited = True
        while True:
            directions = []
            if i > 0 and not self._cell[i - 1][j].visited:
                directions.append("left")
            if i < self._num_cols - 1 and not self._cell[i + 1][j].visited:
                directions.append("right")
            if j > 0 and not self._cell[i][j - 1].visited:
                directions.append("up")
            if j < self._num_rows - 1 and not self._cell[i][j + 1].visited:
                directions.append("down")
            if len(directions) == 0:
                self._draw_cell(i, j)
            
            if not directions:
                self._draw_cell(i, j)  # draw the current cell
                return
            
            direction = random.choice(directions)
            if direction == "left":
                self._cell[i][j].has_left_wall = False
                self._cell[i - 1][j].has_right_wall = False
                self._break_walls_r(i - 1, j)
            elif direction == "right":
                self._cell[i][j].has_right_wall = False
                self._cell[i + 1][j].has_left_wall = False
                self._break_walls_r(i + 1, j)
            elif direction == "up":
                self._cell[i][j].has_top_wall = False
                self._cell[i][j - 1].has_bottom_wall = False
                self._break_walls_r(i, j - 1)
            elif direction == "down":
                self._cell[i][j].has_bottom_wall = False
                self._cell[i][j + 1].has_top_wall = False
                self._break_walls_r(i, j + 1)

            self._break_walls_r(i, j)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cell[i][j].visited = False

    
