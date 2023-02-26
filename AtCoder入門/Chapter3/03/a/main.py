#!/usr/bin/env python3

import math


def main():
    h, a = map(int, input().split())

    print(math.ceil(h / a))


if __name__ == "__main__":
    main()
