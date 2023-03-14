import re

def main():
    print(max(list(len(i) for i in re.findall('[ACGT]*', input()))))

if __name__ == '__main__':
    main()