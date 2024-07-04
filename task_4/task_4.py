import argparse


def minimum_move(nums):
    nums.sort()  # отсортируем числа в списке по возрастанию
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Вычисление минимального количества ходов")
    parser.add_argument("-n", nargs="+", type=int, help="Список целых чисел")
    parser.add_argument("-v", help="Детальный вывод", action="store_true")
    args = parser.parse_args()

    moves = minimum_move(args.n)

    if args.v:
        print(f"Минимальное количество ходов: {moves}")
    else:
        print(moves)
