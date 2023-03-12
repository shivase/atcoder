#!/usr/bin/env python3 
def main():
    N = int(input())

    cnt = [divCnt(n) for n in range(1,N+1)]

    print(cnt.index(max(cnt)) + 1)

def divCnt(num):
    cnt=0
    while num % 2  == 0 and num > 0:
        cnt += 1
        num /= 2

    return cnt

if __name__ == '__main__':
    main()