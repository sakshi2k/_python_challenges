def median(a: int, b: int, c: int) -> int:
    if (a >= b and a <= c) or (a <= b and a >= c):
        return a
    elif (b >= a and b <= c) or (b <= a and b >= c):
        return b
    return c


def find_min(a:int, b:int, c:int) -> int:
    if (a <= b and a <= c):
        return a
    elif (b <= a and b <= c):
        return b
    return c


def find_max(a:int, b:int, c:int) -> int:
    if (a >= b and a >= c):
        return a
    elif (b >= a and b >= c):
        return b
    return c


def median2(a: int, b: int, c: int) -> int:
    min_of_three = find_min(a, b, c)
    max_of_three = find_max(a, b, c)
    return a + b + c - min_of_three - max_of_three


if __name__ == "__main__":
    print(median(10, 0, 5))
    print(median2(10, 0, 5))

    print(median(0, 0, 0))
    print(median2(0, 0, 0))

    print(median(10, 40, 50))
    print(median2(10, 40, 50))
