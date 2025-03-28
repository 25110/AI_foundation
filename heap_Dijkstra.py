import heapq
n,m=map(int, input().split())
way=dict()
length=[]
hp=[]
for i in range(0,n+1):
    way[i]=[]
    length.append(-1)
length[1]=0
for i in range(m):
    a,b,z=map(int, input().split())
    way[a].append((b,z))
t=1
heapq.heappush(hp,(0,1))
length[0]=10000000000
while(len(hp)):
    l,t=heapq.heappop(hp)
    for j in way[t]:
        if(length[j[0]]==-1 or length[t]+j[1]<length[j[0]]):
            length[j[0]]=length[t]+j[1]
            heapq.heappush(hp,(length[j[0]],j[0]))
print(length[n])