import unittest
from main import Runner, Tournament  # импортируем классы Runner и Tournament из файла main


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner("test walk")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)  # методом assertEqual сравните distance со значением 50

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner("test run")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)  # методом assertEqual сравните distance со значением 100

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner("runner1")
        runner2 = Runner("runner2")
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)  # расстояния не равны после 10 пробежек и 10 прогулок


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # словарь в который сохраняются результаты всех тестов.

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)  # Бегун по имени Усэйн, со скоростью 10.
        self.andrey = Runner("Андрей", speed=9)  # Бегун по имени Андрей, со скоростью 9.
        self.nick = Runner("Ник", speed=3)  # Бегун по имени Ник, со скоростью 3.

    @classmethod
    def tearDownClass(cls):  # метод, где выводятся all_results по очереди в столбец.
        print("\nРезультаты:")
        for test_name, result in cls.all_results.items():
            print(f"{test_name} - {result}")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results["Забег Усэйн и Ник"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results["Забег Андрей и Ник"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results["Забег Усэйн, Андрей и Ник"] = {place: str(runner) for place, runner in
                                                                   results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")


if __name__ == "__main__":
    unittest.main()
