def main():
    A,B,C = map(int, input().split())

    cnt = 0
    while check(A,B,C):
        cnt += 1
        x, y, z = divide(A,B,C)
        if x == A and y == B and z ==C:
            cnt = -1
            break
        else:
            A = x
            B = y
            C = z

    print(cnt)

def check(a,b,c):
    if a%2==0 and b%2==0 and c%2==0:
        return True
    return False

def divide(a,b,c):
    x = b/2 + c/2
    y = a/2 + c/2
    z = a/2 + b/2

    return x,y,z

if __name__ == '__main__':
    main()