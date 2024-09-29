def factorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res *= i

    return res


def sum_of_factorial(l: list[int]) -> int:
    res = 0
    for val in l:
        res += factorial(val)
    return res


def main() -> None:
    print(sum_of_factorial([1, 2, 3]))
    print(sum_of_factorial([1, 2, 3, 4]))
    print(sum_of_factorial([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()
