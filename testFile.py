import unittest
import Working_SOS_Game


class testingClass(unittest.TestCase):
    def testBoardSize(self):
        a = Working_SOS_Game.retBoardEntry()
        b = Working_SOS_Game.mSpots.len()
        self.assertEqual(a ^ 2, b)

    def turnTest(self):
        xTurn = whoseTurn
        self.assertEqual(whoseTurn, True)

    def testGameType(self):
        Working_SOS_Game.simpleGame = r1.text()
        self.assertEqual(simpleGame, 'Simple Game')


if __name__ == '__main__':
    unittest.main()
