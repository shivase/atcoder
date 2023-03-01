#!/usr/bin/env python3

def main():
    S = input()

    length = len(S)

    strings = []
    tmp = ''
    for i in range(length):
        tmp = tmp + S[i]
        if len(tmp) > 1 and S[i].isupper():
            strings.append(tmp)
            tmp = ''

    strings = sorted(strings, key=str.lower)
    print(''.join(strings))


if __name__ == '__main__':
    main()