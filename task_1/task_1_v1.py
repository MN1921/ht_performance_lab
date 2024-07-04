from typing import TypeAlias
import argparse

CircularArraySlice: TypeAlias = list[int]
CircularArraySliceList: TypeAlias = list[CircularArraySlice]


class CircularArray:
    def __init__(self, length: int):
        self.start = 1
        self.length = length
        self.array = [i for i in range(self.start, self.length+1)]


def generate_all_circular_array_slice(
        circular_array: CircularArray,
        length: int
):
    start = 0
    circular_array_slice_list = list()
    while True:
        index, circular_array_slice = generate_circular_array_slice(
            circular_array,
            start,
            length
        )
        circular_array_slice_list.append(circular_array_slice)
        if circular_array_slice[-1] == circular_array.start:
            break
        start = index
    return circular_array_slice_list


def get_circular_array_path(
    circular_array_slice_list: CircularArraySliceList
):
    path = list()
    for circular_array_slice in circular_array_slice_list:
        path.append(str(circular_array_slice[0]))
    return "".join(path)


def generate_circular_array_slice(
    circular_array: CircularArray,
    start: int,
    length: int
):
    circular_array_slice = list()
    index = start
    for _ in range(length):
        if index >= circular_array.length:
            index = 0
        item = circular_array.array[index]
        circular_array_slice.append(item)
        index += 1
    index = index - 1
    return index, circular_array_slice


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Определение последовательности шагов")
    parser.add_argument("-m", help="Интервал длины обхода", required=True, type=int)
    parser.add_argument("-n", help="Размер кругового массива", required=True, type=int)
    parser.add_argument("-v", help="Детальный вывод", action="store_true")
    args = parser.parse_args()

    # Создаем экземпляр CircularArray
    x = CircularArray(args.n)
    if args.v:
        print("CircularArray:", x.array)

    # Генерируем CircularArraySliceList с заданной длинной CircularArraySlice
    x_slice_list = generate_all_circular_array_slice(x, args.m)
    if args.v:
        print("CircularArraySliceList:", x_slice_list)

    # Формируем путь из CircularArraySliceList
    x_path = get_circular_array_path(x_slice_list)
    if args.v:
        print("CircularArrayPath:", x_path)
    else:
        print(x_path)
