def main():
    N, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    num=0
    sum=0
    for n in a:
        sum += n
        if ( sum > x):
            break
        num += 1

    if sum < x:
        num -= 1

    print(num)

if __name__ == '__main__':
    main()