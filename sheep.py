import random
from directions import Directions


class Sheep:
    def __init__(self, sheep_move_dist, init_pos_limit):
        self._x = random.uniform(-init_pos_limit, init_pos_limit)
        self._y = random.uniform(-init_pos_limit, init_pos_limit)
        self._move_dist = sheep_move_dist

    def move(self):
        direction = random.choice(list(Directions))
        if direction is Directions.NORTH:
            self._y += self._move_dist
        elif direction is Directions.SOUTH:
            self._y -= self._move_dist
        elif direction is Directions.EAST:
            self._x -= self._move_dist
        elif direction is Directions.WEST:
            self._x += self._move_dist

    def get_pos(self):
        return self._x, self._y