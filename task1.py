from typing import List


# Сложность по времени: O(N), т.к у нас используется
# всего один цикл по первому списку,
# а проверка на вхождение элемента в множество составляет O(1)
def get_unique_elements(
        first_array: List[int], second_array: List[int]) -> List[int]:
    second_set = set(second_array)
    return [item for item in first_array if item not in second_set]


# Printing: [2, 3]
print(get_unique_elements([1, 2, 3], [1, 4, 5]))