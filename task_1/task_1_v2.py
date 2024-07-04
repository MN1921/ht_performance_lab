import argparse
#  n - Длинна Кругового Массива
#  m - Интервал обхода Кругового Массива


def circular_sequence(n: int, m: int):
    yield 1
    for i in range(m-1, n*m, m-1):
        v = i % n + 1
        if v == 1:
            return
        yield v


def circular_path(a: list[int]):
    return "".join([str(i) for i in a])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Определение последовательности шагов")
    parser.add_argument("-m", help="Интервал длины обхода", required=True, type=int)
    parser.add_argument("-n", help="Размер кругового массива", required=True, type=int)
    parser.add_argument("-v", help="Детальный вывод", action="store_true")
    args = parser.parse_args()

    x = list(circular_sequence(args.n, args.m))
    p = circular_path(x)

    if args.v:
        print("circular_sequence:", x)
        print(p)
    else:
        print(p)
