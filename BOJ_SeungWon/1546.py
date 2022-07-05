n=int(input())
a=list(map(int,input().split()))
b=[]
for score in a:
    b.append(score/max(a)*100)
print(sum(b)/n)


    
