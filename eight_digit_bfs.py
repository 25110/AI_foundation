from collections import deque
s=input().split(' ')
d=set()
t=deque()
t1=deque()
p=s.index('x')
t.append(tuple(s))
t1.append((p,0))
d.add(tuple(s))
while(len(t)):
    v=t.popleft()
    b,m=t1.popleft()
    x=list(v)
    if(v==('1','2','3','4','5','6','7','8','x')):
        print(m)
        exit()
    if(b-3>=0):
        x[b-3],x[b]=x[b],x[b-3]
        e=tuple(x)
        if(e not in d):
            d.add(e)
            t.append(e)
            t1.append((b-3,m+1))
        x[b-3],x[b]=x[b],x[b-3]
    if(b%3!=0):
        x[b-1],x[b]=x[b],x[b-1]
        e=tuple(x)
        if(e not in d):
            d.add(e)
            t.append(e)
            t1.append((b-1,m+1))
        x[b-1],x[b]=x[b],x[b-1]
    if(b%3!=2):
        x[b+1],x[b]=x[b],x[b+1]
        e=tuple(x)
        if(e not in d):
            d.add(e)
            t.append(e)
            t1.append((b+1,m+1))
        x[b+1],x[b]=x[b],x[b+1]
    if(b+3<9):
        x[b+3],x[b]=x[b],x[b+3]
        e=tuple(x)
        if(e not in d):
            t.append(e)
            t1.append((b+3,m+1))
        x[b+3],x[b]=x[b],x[b+3]
print(-1)