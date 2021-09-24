from collections import namedtuple

Vector2D = namedtuple("Vector2D", ['x', 'y'])

class Player:

    def __init__(self, coords):
        self._pos = Vector2D(*coords)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, coords):
        self._pos = Vector2D(*coords)
