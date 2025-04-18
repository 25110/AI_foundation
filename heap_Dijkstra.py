import heapq
n,m=map(int, input().split())
way=dict()
length=[]
hp=[]
for i in range(0,n+1):
    way[i]=dict()
    length.append(-1)
length[1]=0
for i in range(m):
    a,b,z=map(int, input().split())
    if(way[a].get(b)==None or way[a][b]>z):
        way[a][b]=z
heapq.heappush(hp,(0,1))
length[0]=10000000000
while(len(hp)):
    l,t=heapq.heappop(hp)
    for j in way[t].items():
        if(length[j[0]]==-1 or length[t]+j[1]<length[j[0]]):
            length[j[0]]=length[t]+j[1]
            heapq.heappush(hp,(length[j[0]],j[0]))
print(length[n])