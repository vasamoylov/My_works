import unittest
from tests_12_1 import RunnerTest
from tests_12_2 import TournamentTest

runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runST)




