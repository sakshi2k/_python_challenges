# https://docs.pytest.org/en/stable/getting-started.html
# Find problem statement in md file

def solution(D: list, C: list, P: int):

    count = 0
    n = D.__len__()

    while P > 0:
        count += 1
        next_min_dist = 99999999
        next_min_idx = n

        for i in range(0, n):
            if(C[i] != 0 and D[i] < next_min_dist):
                next_min_dist = D[i]
                next_min_idx = i
        
        if next_min_idx == n:
            break
        
        P -= C[next_min_idx]
        
        C[next_min_idx] = 0

    return count - 1


def main():
    assert solution([5, 11, 1, 3], [6, 1, 3, 2], 7) == 2
    assert solution([10, 15, 1], [10, 1, 2], 3) == 1
    assert solution([11, 18, 1], [9, 18, 8], 7) == 0
    assert solution([1, 4, 2, 5], [4, 9, 2, 3], 19) == 4


if __name__ == "__main__":
    main()