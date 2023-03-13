def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))


    A.append(A[0] + K)

    distance = []
    for n in range(N):
        distance.append(A[n+1] - A[n])


    print( K - max(distance))

if __name__ == '__main__':
    main()