import unittest
import subprocess
from tic_tac_toe import TicTacToe

class TestsTicTacToe(unittest.TestCase):    
    def test_turn(self):
        self.assertEqual(TicTacToe().turn('0'), 'ValError')
        TicTacToe().reset()
        self.assertEqual(TicTacToe().turn('5'), None)
        TicTacToe().reset()
        self.assertEqual(TicTacToe().turn('10'), 'ValError')
        TicTacToe().reset()
        self.assertEqual(TicTacToe().turn('3.5'), 'ValError')
        TicTacToe().reset()
        self.assertEqual(TicTacToe().turn('qwerty'), 'ValError')
        TicTacToe().reset()
        self.assertEqual(TicTacToe().turn('True'), 'ValError')
        TicTacToe().reset()
        self.assertEqual(TicTacToe().turn('False'), 'ValError')
        tic_tac=TicTacToe()
        tic_tac.turn('4')
        self.assertEqual(tic_tac.turn('4'), 'CellOccupied')
    
    def test_reset(self):
        TicTacToe().turn('4')
        TicTacToe().reset()
        self.assertEqual(TicTacToe().turn('4'), None)
    
    def test_game(self):
        tic_tac=TicTacToe()
        turns = ['2', '3', '5', '6', '8']
        for turn in turns:
            tic_tac.turn(turn)
        self.assertEqual(tic_tac.player_flag, False)
        tic_tac.reset()
        turns = ['1', '2', '4', '5', '6', '8']
        for turn in turns:
            tic_tac.turn(turn)
        self.assertEqual(tic_tac.player_flag, True)
        tic_tac.reset()
        turns = ['1', '2', '3', '4', '6', '5', '8', '9', '7']
        for turn in turns[:-1]:
            tic_tac.turn(turn)
        msg=tic_tac.turn(turns[-1])
        self.assertEqual(msg, 'Drawn game')
        


if __name__ == '__main__':
    unittest.main()

