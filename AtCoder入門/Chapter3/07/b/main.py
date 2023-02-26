#!/usr/bin/env python3


def main():
    _ = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    Alice = 0
    Bob = 0
    for index, data in enumerate(a):
        if index % 2:
            Bob += data
        else:
            Alice += data

    print(Alice - Bob)


if __name__ == "__main__":
    main()
