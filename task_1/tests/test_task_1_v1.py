from task_1.task_1_v1 import CircularArray, generate_all_circular_array_slice, get_circular_array_path


# Этот тест проверяет, что экземпляр класса CircularArray инициализируется с правильным массивом чисел
def test_circular_array_initialization():
    circular_array = CircularArray(5)
    assert circular_array.array == [1, 2, 3, 4, 5]


# Этот тест проверяет, что функция возвращает правильный список срезов кругового массива.
def test_generate_all_circular_array_slice():
    circular_array = CircularArray(5)
    slices = generate_all_circular_array_slice(circular_array, 4)
    assert slices == [[1, 2, 3, 4],
                      [4, 5, 1, 2],
                      [2, 3, 4, 5],
                      [5, 1, 2, 3],
                      [3, 4, 5, 1]]


# Этот тест проверяет, что функция возвращает правильный путь, сформированный из списка срезов кругового массива.
def test_get_circular_array_path():
    circular_array = CircularArray(5)
    slices = generate_all_circular_array_slice(circular_array, 4)
    path = get_circular_array_path(slices)
    assert path == "14253"
