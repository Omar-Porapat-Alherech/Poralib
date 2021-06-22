import logging

module_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format='| %(asctime)s | %(name)-12s | %(levelname)-8s | %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


# Insertion Sort
# O(1) Space Complexity as it sorts in the array it came from
# o(n) Time best case when array is already sorted.
# o(n^2) worst case/avg , when array is sorted in reverse order
def insertion_sort(input_array, ascending_order=True):
    if ascending_order:
        module_logger.info("Ascending order sort.")
    else:
        module_logger.info("Descending order sort.")
    for arr_pos in range(1, len(input_array)):
        key = input_array[arr_pos]
        arr_pos_left = arr_pos - 1
        if not ascending_order:
            while input_array[arr_pos_left] < key and arr_pos_left >= 0:
                input_array[arr_pos_left + 1] = input_array[arr_pos_left]
                arr_pos_left -= 1
        else:
            while input_array[arr_pos_left] > key and arr_pos_left >= 0:
                input_array[arr_pos_left + 1] = input_array[arr_pos_left]
                arr_pos_left -= 1
        input_array[arr_pos_left + 1] = key
    return input_array


if __name__ == "__main__":
    pass
