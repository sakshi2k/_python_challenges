def transform_to_dual(dec: int) -> str:
    if dec == 0:
        return "0"
    binary = ""
    while dec > 0:
        binary = str(dec % 2) + binary
        dec = dec // 2
    return binary


if __name__ == "__main__":
    print(transform_to_dual(13))
