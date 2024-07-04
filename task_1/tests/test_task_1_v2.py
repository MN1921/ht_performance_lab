from task_1.task_1_v2 import circular_sequence, circular_path


def test_circular_sequence():
    # Проверяем, что последовательность генерируется корректно
    assert list(circular_sequence(5, 4)) == [1, 4, 2, 5, 3]


def test_circular_path():
    # Проверяем, что путь формируется правильно из последовательности
    p = list(circular_sequence(5, 4))
    assert circular_path(p) == "14253"
