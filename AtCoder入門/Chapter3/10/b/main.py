#!/usr/bin/env python3


def main():
    height, width = map(int, input().split())

    array = []
    array.append([" "] * (width + 2))
    for h in range(height):
        array.append([" "] + list(input()) + [" "])
    array.append([" "] * (width + 2))

    for h in range(1, height + 1):
        for w in range(1, width + 1):
            count = 0
            if array[h][w] == "#":
                continue
            if array[h - 1][w - 1] == "#":
                count += 1
            if array[h - 1][w] == "#":
                count += 1
            if array[h - 1][w + 1] == "#":
                count += 1
            if array[h][w - 1] == "#":
                count += 1
            if array[h][w + 1] == "#":
                count += 1
            if array[h + 1][w - 1] == "#":
                count += 1
            if array[h + 1][w] == "#":
                count += 1
            if array[h + 1][w + 1] == "#":
                count += 1

            array[h][w] = str(count)

    for h in range(1, height + 1):
        print("".join(array[h]).strip())


if __name__ == "__main__":
    main()
