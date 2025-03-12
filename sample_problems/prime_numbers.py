def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    for i in range(2, (n // 2) + 1):
        if (n % i) == 0:
            return False
    return True


def next_prime(n: int) -> int:
    if n <= 2:
        return 2
    
    if is_prime(n):
        return n
    
    if n % 2 == 0:
        n += 1 
    
    while not is_prime(n):
        n += 2 
    return n
    

if __name__ == "__main__":
    test_prime_numbers_or_not = [1, 2, 3, 4, 5, 7, 16, 17, 118, 119, 120]
    for num in test_prime_numbers_or_not:
        print(f"is_prime({num}) = {is_prime(num)}")

    test_next_prime = [0, 1, 2, 4, 10, 14, 20, 30, 50]
    for i in test_next_prime:
        print(f"next_prime({i}) = {next_prime(i)}")

        