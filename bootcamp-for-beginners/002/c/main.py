#!/usr/bin/env python3


def main():
    _ = input()
    x = list(map(int, input().split()))

    left = min(x)
    right = max(x)

    stamina_min = None

    for i in range(left, right + 1):
        stamina = 0
        for p in x:
            stamina += (i - p) ** 2

        if stamina_min is None:
            stamina_min = stamina
        elif stamina < stamina_min:
            stamina_min = stamina

    print(stamina_min)


if __name__ == "__main__":
    main()
