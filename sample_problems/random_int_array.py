import random


def create_random(n: int) -> list[int]:
    """Creates an array with `n` random integers in the range `[5, 99]`"""
    a_list = []
    for i in range(n):
        a_list.append(random.randint(5, 99))

    return a_list


def to_string(a: list[int]) -> str:
    return str(a)


def pos_min(a: list[int]) -> int:
    """Returns the position of the smallest element in list a"""
    min_idx: int = 0
    for i in range(0, a.__len__()):
        if (a[i] < a[min_idx]): 
            min_idx = i

    return min_idx


def swap(a: list[int]) -> None:
    """Swaps the first and last element in `a`."""
    temp = a[0]
    a[0] = a[a.__len__() - 1]
    a[a.__len__() - 1] = temp


if __name__ == "__main__":
    a = create_random(10)
    print(a)
    print(pos_min(a))
    swap(a)
    print(a)
