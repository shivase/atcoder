#!/usr/bin/env python3

import math

def main():
    N, Y = map(int, input().split())
    x, y, z = -1, -1 , -1

    for a in range(N+1):
        for b in range(N+1):
            c = N - a - b
            if c < 0 or  N < c:
                continue
            if a * 10000 + b * 5000 + c * 1000 == Y:
                x, y, z = a, b, c
                break
        if x > -1 or y > -1 or z > -1:
            break


    print(x,y,z)

if __name__ == '__main__':
    main()