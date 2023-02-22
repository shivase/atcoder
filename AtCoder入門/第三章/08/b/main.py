#!/usr/bin/env python3


def main():
    s = input()

    result = False

    if s[0] == "A":
        if hasCstr(s[2:-1]):
            s = s.lstrip("A")
            s = s[0] + s[1:-1].replace("C", "") + s[-1]
            if s.islower():
                result = True

    print("AC" if result else "WA")


def hasCstr(string):
    result = False

    for x in string:
        if x == "C":
            if result is True:
                return False
            else:
                result = True

    return result


if __name__ == "__main__":
    main()
