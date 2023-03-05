import math;
def main():
    N = int(input())

    X = math.ceil(N * 100 / 108)
    N2 = math.floor(X*1.08)

    if  N2 == N:
        print(X)
    else:
        print(':(')


if __name__ == '__main__':
    main()
