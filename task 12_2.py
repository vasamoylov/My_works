import tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = tournament.Runner('Усейн', 10)
        self.runner2 = tournament.Runner('Андрей', 9)
        self.runner3 = tournament.Runner('Ник', 3)

    def tearDown(self):
        print(self.all_results)

    def test_first(self):
        tournament1 = tournament.Tournament(90, self.runner1, self.runner3)
        self.all_results.update(tournament1.start())
        last_runner = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_runner == 'Ник')

    def test_second(self):
        tournament2 = tournament.Tournament(90, self.runner2, self.runner3)
        self.all_results.update(tournament2.start())
        last_runner = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_runner == 'Ник')

    def test_third(self):
        tournament3 = tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results.update(tournament3.start())
        last_runner = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_runner == 'Ник')


if __name__ == "__main__":
    unittest.main()
