import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walker = runner.Runner('first')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_ = runner.Runner('second')
        for i in range(10):
            runner_.run()
        self.assertEqual(runner_.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walker = runner.Runner('first')
        runner_ = runner.Runner('second')
        for i in range(10):
            walker.walk()
        first = walker.distance
        for i in range(10):
            runner_.run()
        second = runner_.distance
        self.assertNotEqual(first, second, msg=None)


if __name__ == "__main__":
    unittest.main()
