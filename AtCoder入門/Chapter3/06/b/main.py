#!/usr/bin/env python3


def main():
    _ = int(input())
    a = list(map(int, input().split()))

    count = 0
    while isAllEven(a):
        a = list(map(lambda x: x / 2, a))
        count += 1

    print(count)


def isAllEven(values):

    ret = True
    for value in values:
        if value % 2 != 0:
            ret = False
            break

    return ret


if __name__ == "__main__":
    main()
