def main():
    N = int(input())
    V = list(map(int, input().split()))

    V.sort()
    value = V[0]
    for v in V[1:]:
        value = (value+v) / 2

    print(value)


if __name__ == '__main__':
    main()