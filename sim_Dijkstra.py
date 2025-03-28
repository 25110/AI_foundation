n,m=map(int, input().split())
way=[]
length=[]
arrive=[]
for i in range(0,n+1):
    way.append([])
    length.append(-1)
    arrive.append(0)
    for j in range(0,n+1):
        way[i].append(-1)
length[1]=0
for i in range(m):
    a,b,z=map(int, input().split())
    way[a][b]=z
t=1
arrive[t]=1
length[0]=100000000
for i in range(2,n+1):
    for j in range(1,n+1):
        if(way[t][j]!=-1 and length[t]!=-1 and (length[t]+way[t][j]<length[j] or length[j]==-1)):
            length[j]=length[t]+way[t][j]
    t=0
    for j in range(2,n+1):
        if(arrive[j]!=1 and length[j]!=-1 and length[t]>length[j]):
            t=j
    arrive[t]=1
print(length[n])