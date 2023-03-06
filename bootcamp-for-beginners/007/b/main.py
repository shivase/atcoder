def main():
    A = [list(map(int, input().split())) for n in range(3)]
    N = int(input())
    b = [int(input()) for n in range(N)]

    card = [[0,0,0],[0,0,0],[0,0,0]]

    for num in b:
        for i, A1 in enumerate(A):
            for j, A2 in enumerate(A1):
                if A2 == num:
                    card[i][j] = 1
    
    if sum(A[0]) == 3 \
        or sum(card[1]) == 3 \
        or sum(card[2]) == 3 \
        or card[0][0]+card[1][0]+card[2][0] == 3 \
        or card[0][1]+card[1][1]+card[2][1] == 3 \
        or card[0][2]+card[1][2]+card[2][2] == 3 \
        or card[0][0]+card[1][1]+card[2][2] == 3 \
        or card[0][2]+card[1][1]+card[2][0] == 3:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__" :
    main()