list=[]
for _ in range(10):
    a=int(input())
    list.append(a%42)
print(len(set(list)))

