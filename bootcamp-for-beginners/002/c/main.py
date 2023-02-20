#!/usr/bin/env python3


def main():
    _ = input()
    x = list(map(int, input().split()))

    results = list()
    for i in range(min(x), max(x) + 1):
        stamina = 0
        for p in x:
            stamina += (i - p) ** 2
        results.append(stamina)

    print(min(results))


if __name__ == "__main__":
    main()
