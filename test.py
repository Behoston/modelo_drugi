# coding=utf-8
import unittest
from copy import deepcopy

from Amino import Amino
from Protein import Protein


class ProteinTest(unittest.TestCase):
    def test_protein_move_shoul_can_be_reverted(self):
        p = Protein('HHHPPPHHH')
        p_copy = deepcopy(p)
        p.move()
        self.assertNotEqual(p, p_copy)
        p.undo_move()
        self.assertEquals(p, p_copy)


class AminoTest(unittest.TestCase):
    def test_eq(self):
        a1 = Amino('H', 0, 0)
        a2 = Amino('H', 0, 0)
        self.assertEquals(a1, a2)

    def test_eq_list(self):
        a1 = [Amino('H', 1, 2)]
        a2 = [Amino('H', 1, 2)]
        self.assertEquals(a1, a2)


if __name__ == '__main__':
    unittest.main()
