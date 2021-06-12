import logging

module_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format='| %(asctime)s | %(name)-12s | %(levelname)-8s | %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


# Quick sort Sort
# O(1) Space Complexity as it sorts in the array it came from
# o(n) Time best case when array is already sorted.
# o(n^2) worst case/avg , when array is sorted in reverse order
def quick_sort(input_array, start, end):
    module_logger.info("Starting quick sort on %s.", input_array)
    if len(input_array) == 1:
        return arr
    if start < end:
        module_logger.info("Finding midpoint for partition.")
        fracture = partition(input_array, start, end)
        module_logger.info("...midpoint found %s", fracture)
        module_logger.info("Recursive quick sort on lower portion - bounds %s to %s - len  %s." % (start, fracture - 1,
                                                                                                   fracture - 1 - start))
        quick_sort(input_array, start, fracture - 1)
        module_logger.info("Recursive quick sort on upper portion - bounds %s to %s - len  %s." % (fracture + 1, end,
                                                                                                   end - fracture + 1))
        quick_sort(input_array, fracture + 1, end)
        module_logger.info("Complete!")



def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def partition(arr, start, end):
    pivot = arr[end]
    arr_pos_left = start - 1
    for arr_pos in range(start, end):
        if arr[arr_pos] <= pivot:
            arr_pos_left += 1
            swap(arr, arr_pos, arr_pos_left)
    swap(arr, arr_pos_left+1, end)
    return arr_pos_left + 1

if __name__ == "__main__":
    pass
