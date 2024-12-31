import unittest
from main import Runner, Tournament  # импортируем класс Runner из файла main

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {} # словарь в который сохраняются результаты всех тестов.

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10) # Бегун по имени Усэйн, со скоростью 10.
        self.andrey = Runner("Андрей", speed=9) # Бегун по имени Андрей, со скоростью 9.
        self.nick = Runner("Ник", speed=3) # Бегун по имени Ник, со скоростью 3.

    @classmethod
    def tearDownClass(cls): # метод, где выводятся all_results по очереди в столбец.
        print("\nРезультаты:")
        for test_name, result in cls.all_results.items():
            print(f"{test_name} - {result}")

    def test_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results["Забег Усэйн и Ник"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results["Забег Андрей и Ник"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results["Забег Усэйн, Андрей и Ник"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")


if __name__ == "__main__":
    unittest.main()
