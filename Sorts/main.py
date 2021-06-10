# Insertion Sort
# O(1) Space Complexity as it sorts in the array it came from, besides the fact that python is pass by value.
# TODO Complete comments + implement tests.
def insertion_sort(input_array, ascending_order=True):
    for arr_pos in range(1, len(input_array)):
        key = input_array[arr_pos]
        arr_pos_left = arr_pos - 1
        x = input_array[arr_pos_left]
        comparison = input_array[arr_pos_left] > key and arr_pos_left >= 0
        # We can sort in descending order
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_arr = [10, 50, 20, 5, 100, 23, 65, 15]
    x = insertion_sort(input_arr, ascending_order=False)
    print(input_arr)
    print(x)
