#!/usr/bin/env python3

from collections import defaultdict
# from collections import Counter

def main():
    N = int(input())

    S = [''.join(sorted(input())) for s in range(N)]
    dict = defaultdict(int)

    for str in S:
        dict[str] +=1

    ans = sum([dict[ind]*(dict[ind]-1)//2 for ind in dict])

    # num = Counter(S)
    # print(sum(n(n-1) // 2 for n in num.values()))

    print(ans)


if __name__ == '__main__':
    main()