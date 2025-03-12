def interleave(a: list[int], b: list[int]) -> list[int]:
    """
    Returns a new array with elements consecutively taken from array `a` and
    `b`.
    """
    res = []
    for i in range(0, a.__len__()):
        res.append(a[i])
        res.append(b[i])
    return res


def perfect_shuffle(a: list[int]) -> list[int]:
    """Returns a new array that is perfectly shuffled once."""
    # a = [1,2,3,4,5,6,7,8,9,10]
    b = a[a.__len__() // 2: a.__len__()]
    a = a[0: a.__len__() // 2]

    return interleave(a, b)


def shuffle_number(a: int) -> int:
    """Returns the number of perfect shuffles needed to get to the same array."""
    b1 = []
    for i in range(0, a):
        b1.append(i)
        i += 1

    b2 = perfect_shuffle(b1)
    count = 1

    while (b2 != b1):
        b2 = perfect_shuffle(b2)
        # print(b2)
        count += 1

    return count


if __name__ == "__main__":
    print(shuffle_number(1024))