def is_prime_number(n: int) -> bool:
    if n == 0 or n == 1:
        return False
    if (n <= 3):
        return True
    for i in range(2, (n // 2) + 1):
        if (n % i == 0):
            return False
        i += 1
    return True


# Prime Twins are pairs of natural numbers  such that p+2=q and both p and q are prime numbers
def prime_twins(n: int) -> list[tuple[int, int]]:
    """Returns the first n prime twins."""
    i = 3
    result_list: list[tuple] = []
    while (result_list.__len__() < n):
        if is_prime_number(i) and is_prime_number(i + 2):
            result_list.append((i, i + 2))

        i += 1

    return result_list


def prime_triplets(n: int) -> list[tuple[int, int, int]]:
    """Returns the first n prime triplets."""
    i = 3
    result_list: list[tuple] = []
    while (result_list.__len__() < n):
        if is_prime_number(i) and is_prime_number(i + 6):
            x = 0
            if (is_prime_number(i + 2)):
                x = i + 2
            elif (is_prime_number(i + 4)):
                x = i + 4

            if x != 0:
                result_list.append((i, x, i + 6))

        i += 1

    return result_list


if __name__ == "__main__":
    # prime_num_test_cases = [2,3,4,5,6,7,8,10,11,12]
    # for i in range(0, prime_num_test_cases.__len__()):
    #     print(f"i : {prime_num_test_cases[i]}, {is_prime_number(prime_num_test_cases[i])}")
    #     i+=1

    # prime_twins_test_cases = 4
    # print(f"prime_twins_test_cases = {prime_twins_test_cases}, {prime_twins(prime_twins_test_cases)}")

    # prime_triplets_test_cases = 3
    # print(f"prime_triplets_test_cases = {prime_triplets_test_cases}, {prime_triplets(prime_triplets_test_cases)}")

    assert prime_twins(2) == [(3, 5), (5, 7)]
    assert prime_triplets(10) == [(5, 7, 11), (7, 11, 13), (11, 13, 17), (13, 17, 19), (
        17, 19, 23), (37, 41, 43), (41, 43, 47), (67, 71, 73), (97, 101, 103), (101, 103, 107)]
