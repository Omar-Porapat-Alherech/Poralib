import logging
import unittest

from Poralib.Sorts.quick_sort import quick_sort

module_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format='| %(asctime)s | %(name)-12s | %(levelname)-8s | %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


class QuickSortTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.already_sorted = [10, 20, 30, 40, 50, 60]
        cls.not_already_sorted_t1  = [30, 20, 50, 60, 40, 10]
        cls.not_already_sorted_t2 = [30, 20, 50, 60, 40, 10]
        cls.start = 0
        cls.end = 6

    def test_quick_sort(self):
        module_logger.info("Testing quick sort.")
        quick_sort(self.not_already_sorted_t1, self.start, self.end - 1)
        self.assertEqual(self.already_sorted, self.not_already_sorted_t1)
        module_logger.info("Passed.")

    def test_quick_already_sorted(self):
        module_logger.info("Testing quick sort when input is already sorted.")
        quick_sort(self.not_already_sorted_t2, self.start, self.end - 1)
        self.assertEqual(self.already_sorted, self.not_already_sorted_t2)
        module_logger.info("Passed.")


if __name__ == '__main__':
    unittest.main()
