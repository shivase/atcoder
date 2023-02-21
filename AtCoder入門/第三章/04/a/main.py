#!/usr/bin/env python3


def main():
    k = int(input())
    a, b = map(int, input().split())

    result = False
    for i in range(a, b + 1):
        if i % k == 0:
            result = True
            break

    print("OK" if result else "NG")


if __name__ == "__main__":
    main()
