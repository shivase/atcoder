
def main():
    N, A, B = map(int,input().split())
    S = list(input())

    sum = 0
    b_rank = 1

    for p in S:
        if  p == 'a':
            if ( sum < A + B):
                sum += 1
                print('Yes');
            else:
                print('No')
        if p == 'b':
            if  sum < A + B and b_rank <=  B:
                sum += 1
                b_rank += 1
                print('Yes')
            else:
                print('No')
        if p == 'c':
            print('No')


if __name__ == '__main__':
    main()