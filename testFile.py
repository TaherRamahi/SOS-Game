
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

class testAIFeat(unittest.TestCase):
    def testisAI(self):
        temp = player1.isThisCom
        self.assertEqual(temp, True)
    def testBothAI(self):
        temp = player1.isThisCom
        temp2 = player2.isThisCom

        self.assertEqual(temp, True)
        self.assertEqual(temp2, True)

if __name__ == '__main__':
    unittest.main()


