def main():
    N = int(input())
    K = int(input())
    X = map(int, input().split())

    sum=0
    for x in X:
        if x  < K - x:
            sum += 2*x
        else:
            sum += 2*(K-x)

    #sum += 2 * min( abs(x), abs(K-x) )

    print(sum)


if __name__ == "__main__":
    main()