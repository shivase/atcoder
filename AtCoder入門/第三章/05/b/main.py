#!/usr/bin/env python3


def main():
    n, a, b = map(int, input().split())

    sum = 0
    for i in range(n + 1):
        cnt = count(i)
        if a <= cnt <= b:
            sum += i

    print(sum)


# 123 -> 1 + 2 + 3
def count(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10

    return sum


if __name__ == "__main__":
    main()
