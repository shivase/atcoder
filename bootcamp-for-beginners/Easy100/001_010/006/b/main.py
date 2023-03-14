import math

def main():
    H, W = map(int, input().split())

    if H == 1 or W == 1:
        print(1)
    else:
        num = math.ceil(H * W / 2)
        print(num)


if __name__ == '__main__':
    main()