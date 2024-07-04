from task_4.task_4 import minimum_move  # Импортируйте вашу функцию


def test_minimum_move():
    # Подготовка данных для теста
    nums = [1, 10, 2, 9]
    expected_moves = 16  # Ожидаемое количество перемещений

    # Вызов функции и проверка результата
    result = minimum_move(nums)
    assert result == expected_moves, f"Ожидаемое количество перемещений: {expected_moves}, получено: {result}"
