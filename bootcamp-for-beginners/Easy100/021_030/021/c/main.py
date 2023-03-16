import math
def main():
    X = int(input())

    while True:
        sosu = True
        for i in range(2,int(X**(1/2)+1)):
            if ( X % i == 0):
                sosu = False
                X = X + 1
                break;
        if sosu:
            print(X)
            break



if __name__ == '__main__':
    main()