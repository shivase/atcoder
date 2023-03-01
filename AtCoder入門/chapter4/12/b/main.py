#!/usr/bin/env python3

def main():
    n = int(input())
    num = {}

    for _ in range(n):
        num[input()] = 1

    print(len(num))

    # S = set(input() for i in range(n))
    # print(len(S))


if __name__ == '__main__':
    main()