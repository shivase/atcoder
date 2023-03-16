def main():
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))

    left = 0
    for i in range(1,X):
        if i in A:
            left += 1

    right=0
    for i in range(X+1, N):
        if i in A:
            right += 1

    print(min(right,left))


if __name__ == '__main__':
    main()