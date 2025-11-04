from typing import MutableSequence


def bubble_sort(data: MutableSequence) -> None:
    """Sorts a mutable sequence (eg. list or array) in place."""

    for sorted_partition in range(len(data) - 1, 0, -1):
        swapped = False
        for i in range(sorted_partition):
            if data[i] > data[i + 1]:  # No swap if ==. This is important for stability.
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True

        # print(f"End of pass {sorted_partition}.  `data` is now {data}")
        if not swapped:
            # The last pass resulted in no swaps.
            # The data is now sorted.
            break


if __name__ == '__main__':
    from array import array
    # numbers = array('i', [20, 35, -15, 7, 55, 1, -22])
    # numbers = [20, 35, -15, 7, 55, 1, -22]
    # numbers = [-15, -22, 20, 35, 1, 55, 7]
    numbers = [8, 1, 2, 3, 4, 5, 6, 7]

    print(f"Sorting {numbers}")
    bubble_sort(numbers)
    print(f"The sorted data is {numbers}")
