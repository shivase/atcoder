def main():
    s = int(input())

    result = [s]
    for n in range(1,1000000):
        next = fun(result[-1])
        if next in result:
            print(n+1)
            break
        else:
            result.append(next)

def fun(n):
    if n % 2 == 0:
        return n / 2

    return 3 * n + 1

if __name__ == '__main__':
    main()