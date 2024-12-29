import unittest
from main import Runner  # импортируем класс Runner из файла main

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("test walk")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50) # методом assertEqual сравните distance со значением 50

    def test_run(self):
        runner = Runner("test run")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100) # методом assertEqual сравните distance со значением 100

    def test_challenge(self):
        runner1 = Runner("runner1")
        runner2 = Runner("runner2")
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance) # расстояния не равны после 10 пробежек и 10 прогулок

if __name__ == "__main__":
    unittest.main()