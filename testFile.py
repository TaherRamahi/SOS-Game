
import unittest
from Working_SOS_Game import *

class testingClass(unittest.TestCase):
    def testBoardSize(self):
        a = retBoardEntry()
        b = mSpots.len()
        self.assertEqual(a ^ 2, b)

    def turnTest(self):
        xTurn = whoseTurn
        self.assertEqual(whoseTurn, True)

    def testGameType(self):
        simpleGame = r1.get()
        self.assertEqual(simpleGame, 50)

    def testgameInitialized(self):
        gameIntCheck = gameRan
        self.assertEqual(gameIntCheck, True)




class testGeneralGameTest(unittest.TestCase):
    def testBoardSize(self):
        a = retBoardEntry()
        b = mSpots.len()
        self.assertEqual(a ^ 2, b)

    def turnTest(self):
        xTurn = whoseTurn
        self.assertEqual(whoseTurn, True)

    def testGameType(self):
        simpleGame = r1.get()
        self.assertEqual(simpleGame, 50)

    def testgameInitialized(self):
        gameIntCheck = gameRan
        self.assertEqual(gameIntCheck, True)



if __name__ == '__main__':
    unittest.main()
