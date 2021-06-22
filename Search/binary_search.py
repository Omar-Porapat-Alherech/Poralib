import logging

module_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format='| %(asctime)s | %(name)-12s | %(levelname)-8s | %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


# Binary Search
# O(1) Space Complexity as it sorts in the array it came from
# o(1) Best case when the element you want is in the middle
# o(log n) worst case/avg , when array is sorted in reverse order
def binary_search(input_array, start, end, target):
    if end >= start:
        midpoint = (end + start) // 2
        if input_array[midpoint] == target:
            return midpoint
        elif input_array[midpoint] > target:
            return binary_search(input_array, start, midpoint - 1, target)
        else:
            return binary_search(input_array, midpoint + 1, end, target)
    else:
        return -1


if __name__ == "__main__":
    arr = [1, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(arr, 0, len(arr) - 1, 1))
    pass
