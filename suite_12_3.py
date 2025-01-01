import unittest
import tests_12_3


mainST = unittest.TestSuite()
mainST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
mainST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(mainST)