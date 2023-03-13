def main():
    N, K = map(int, input().split())

    num = N % K

    diff = abs(K - num)

    print(min(num,diff))

if __name__ == '__main__':
    main()