def search_linear(a: list[str], item: str) -> int | None:
    """Searches the list for item linearly. Returns the position of item."""
    for i in range(0, a.__len__()):
        if (a[i] == item):
            return i

    return None


def search_binary(a: list[str], item: str) -> int | None:
    """Searches the list for item binary. Returns the position of item."""
    low, high = 0, len(a) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == item:
            return mid  # Found the item at index mid
        elif a[mid] < item:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half
    
    return None 


def search_linear_cmp_count(a: list[str], item: str) -> int:
    """Searches the list for item linearly. Returns the number of comparisions needed."""
    count = 0
    for i in range(0, a.__len__()):
        if (a[i] == item):
            return count
        count += 1

    return count


def search_binary_cmp_count(a: list[str], item: str) -> int:
    """Searches the list for item linearly. Returns the number of comparisions needed."""
    low, high = 0, len(a) - 1
    count = 0
    
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == item:
            return mid  # Found the item at index mid
        elif a[mid] < item:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half
        count += 1
    
    return count


if __name__ == "__main__":
    print(search_linear(["aa", "bb", "cc"], "bb"))
    print(search_linear(["aa", "bb", "cc"], "cc"))
    print(search_linear(["aa", "bb", "cc"], "aa"))
    print(search_linear(["aa", "bb", "cc"], "da"))

    print("\n")

    print(search_binary(["aa", "bb", "cc"], "bb"))
    print(search_binary(["aa", "bb", "cc"], "cc"))
    print(search_binary(["aa", "bb", "cc"], "aa"))
    print(search_binary(["aa", "bb", "cc"], "da"))

    print("\n")

    print(search_linear_cmp_count(["aa", "bb", "cc"], "aa"))
    print(search_linear_cmp_count(["aa", "bb", "cc"], "da"))

    print("\n")

    print(search_binary_cmp_count(["aa", "bb", "cc"], "aa"))
    print(search_binary_cmp_count(["aa", "bb", "cc"], "da"))