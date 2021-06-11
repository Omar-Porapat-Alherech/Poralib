import unittest
import logging
from Poralib.Sorts.insertion_sort import insertion_sort

module_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


class InsertionSortTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.already_sorted = [10, 20, 30, 40, 50, 60]
        cls.not_already_sorted = [30, 20 , 50 ,60, 40 ,10]
        cls.reverse_sorted = [60, 50, 40, 30, 20, 10]

    def test_insertion_sort_already_sorted(self):
        module_logger.log("Testing insertion sort when the array is already sorted. (n) - Best case.")
        self.assertEqual(self.already_sorted, insertion_sort(self.not_already_sorted))
        module_logger.log("Passed.")

    def test_reverse_insertion_sort(self):
        module_logger.log("Testing insertion sort reversed.")
        self.assertEqual(self.reverse_sorted, insertion_sort(self.not_already_sorted, ascending_order=False))
        module_logger.log("Passed.")

if __name__ == '__main__':
    unittest.main()
