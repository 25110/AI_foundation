from queue import Queue
n,m=map(int, input().split())
way=dict()
for i in range(1,n+1):
    way[i]=[]
for i in range(m):
    a,b=map(int, input().split())
    way[a].append(b)
q=Queue()
q.put((1,0))
while(not q.empty()):
    x=q.get()
    p=x[0]
    l=x[1]
    if(l>=n):
        continue
    if(p==n):
        print(l)
        exit()
    for i in range(len(way[p])):
        q.put((way[p][i],l+1))
print(-1)