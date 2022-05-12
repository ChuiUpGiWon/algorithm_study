#220512
#과자가격 K, 과자개수 N, 가진 돈 M

k,n,m=map(int,input().split())
money=(k*n)-m
if money>0:
    print(money)
else:
    print(0)

