n=int(input())
i=2
while n!=1:
    if n%i==0:
        print(i)
        n=n//i # // : 나누기 연산 호 몫의 정수부분만
    else:
        i+=1


