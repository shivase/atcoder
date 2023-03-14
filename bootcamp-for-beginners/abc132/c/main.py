import math

def main():
    N = int(input())
    d = list(map(int, input().split()))

    if (len(d) % 2 == 1):
        print(0)
    else:
        d.sort()
        start = int(len(d) / 2 - 1)
        end =  start + 1
        print(d[end] - d[start])

if __name__ == '__main__':
    main()