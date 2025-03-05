from graphics import Point, Line

class Cell:
    def __init__(self, win=None, visited=False):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = visited


    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return  # don't draw if we don't have a window
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        top_left = Point(self._x1, self._y1)
        bottom_right = Point(self._x2, self._y2)

        left_wall = Line(Point(top_left.x, top_left.y), Point(top_left.x, bottom_right.y))
        top_wall = Line(Point(top_left.x, top_left.y), Point(bottom_right.x, top_left.y))
        right_wall = Line(Point(bottom_right.x, top_left.y), Point(bottom_right.x, bottom_right.y))
        bottom_wall = Line(Point(top_left.x, bottom_right.y), Point(bottom_right.x, bottom_right.y))

        if self.has_left_wall:
            self._win.draw_line(left_wall)
        else:
            self._win.draw_line(left_wall, "white")
        if self.has_top_wall:
            self._win.draw_line(top_wall)
        else:
            self._win.draw_line(top_wall, "white")
        if self.has_right_wall:
            self._win.draw_line(right_wall)
        else:
            self._win.draw_line(right_wall, "white")
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall)
        else:
            self._win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2  - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)


