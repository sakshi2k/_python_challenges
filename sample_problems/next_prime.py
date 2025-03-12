# A number is called prime if it has exactly two factors: 1 and itself.

# Write a function is_prime(n: int) -> bool that takes an integer n and returns True if and only if n is prime.
# Write a function next_prime(n: int) -> int that returns the next prime number that is larger than or equal to , i.e. if is prime, return , otherwise return the next larger prime number.
# Within the main function give suitable test cases for your functions.


def is_prime(n: int) -> bool :
    """Returns `True`, if and only if `n` is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    for i in range(2, (n//2)+1):
        # If num is divisible by any number between 2 and n / 2, it is not prime
        if (n % i) == 0:
            return False
    return True

def next_prime(n: int) -> int:
    """Returns the next prime number that is bigger or equal to `n`."""
    if n <= 2 :
        return 2
    
    if is_prime(n):
        return n
    
    if n % 2 == 0:
        n += 1 
    
    while not is_prime(n):
        n += 2 
    return n
    

if __name__ == "__main__":
    # Test is_prime function
    test_prime_numbers_or_not = [1, 2, 3, 4, 5, 7, 16, 17, 118, 119, 120]
    print("\nTesting is_prime function:")
    for num in test_prime_numbers_or_not:
        print(f"is_prime({num}) = {is_prime(num)}")

    # Test next_prime function
    test_next_prime = [0, 1, 2, 4, 10, 14, 20, 30, 50]
    print("\nTesting next_prime function:")
    for i in test_next_prime:
        print(f"next_prime({i}) = {next_prime(i)}")

        