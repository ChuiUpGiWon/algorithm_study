import sys
#1003
input = sys.stdin.readline

T = int(input())

for i in range(T):
    num = int(input())
    zero = [1,0,1]
    one = [0,1,1]

    length = len(zero)
    if length <= num:
        for i in range(length, num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[num], one[num])
