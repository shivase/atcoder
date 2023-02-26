#!/usr/bin/env python3


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())

    count = 0

    for yen500 in range(a + 1):
        for yen100 in range(b + 1):
            for yen50 in range(c + 1):
                if yen500 * 500 + yen100 * 100 + yen50 * 50 == x:
                    count += 1

    print(count)


if __name__ == "__main__":
    main()
