import unittest
import planetoids

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = planetoids.Player([2,3])

    def test_has_pos(self):
        self.assertTrue(hasattr(self.player, "pos"))
        pos = self.player.pos
        self.assertTrue(hasattr(pos, 'x'))
        self.assertTrue(hasattr(pos, 'y'))

    def test_maintains_pos(self):
        self.assertEqual(self.player.pos.x, 2)
        self.assertEqual(self.player.pos.y, 3)
        self.player.pos = [7,9]
        self.test_has_pos()
        self.assertEqual(self.player.pos.x, 7)
        self.assertEqual(self.player.pos.y, 9)

