def is_triangular(n: int) -> bool:
    i = 1
    sum = 0
    while(sum<n):
        sum += i
        i += 1
    
    if(sum == n):
        return True
    return False

if __name__ == "__main__":
    print(is_triangular(1))
    print(is_triangular(2))
    print(is_triangular(3))
    print(is_triangular(4))
    print(is_triangular(14))
    print(is_triangular(15))
