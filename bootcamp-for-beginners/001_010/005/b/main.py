def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for n in range(N)]

    ok=0
    for a in A:
        sum = C
        for index, v in enumerate(a):
            sum += v * B[index]

        if ( sum > 0):
            ok += 1

    print(ok)


if __name__ == '__main__':
    main()