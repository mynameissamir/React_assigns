n=int(input())
arr=[]
d={}
for i in range(n):
    elem=int(input())
    if elem in d:
        d[elem]+=1
    else:
        d[elem]=1
d1=sorted(d.items(),key=lambda x:(x[1],x[0]),reverse=True)
print(d1[0][0])