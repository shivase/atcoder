def main():
    N = int(input())
    A = list(map(int, input().split()))

    num = [0] * N

    for index, a in enumerate(A):
        num[a-1] = index + 1

    print(" ".join(map(str,num)))


if __name__ == '__main__':
    main()