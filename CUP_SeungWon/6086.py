n=int(input())
sum=11
for i in range(1,n):
    sum+=i
    i+=1
    if(sum>=n):
        break
print(sum)
