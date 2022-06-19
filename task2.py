from typing import List


def get_array_without_zero(array: List[int]) -> List[int]:
    error_flag = False
    while not error_flag:
        try:
            array.remove(0)
        except ValueError:
            error_flag = True
    return array


# Printing: [1, 2, 3, 4, 5]
print(get_array_without_zero([0, 1, 2, 3, 0, 4, 5, 0]))