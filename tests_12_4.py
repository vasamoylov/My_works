import logging
import HumanMoveTests
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            walker = HumanMoveTests.Runner('first', -5)
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                walker.walk()
            self.assertEqual(walker.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner_ = HumanMoveTests.Runner(0)
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                runner_.run()
            self.assertEqual(runner_.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
if __name__ == "__main__":
    unittest.main()
