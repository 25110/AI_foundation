l=[0,0,0,0]
p=[]
def legal(l):
    if((l[1]==l[2] and l[0]!=l[1]) or(l[2]==l[3] and l[0]!=l[2]) or l in p):
        return 0
    return 1
def do(x):
    if(x):
        return 0
    return 1
qu=[]
qu.append(tuple(l))
p.append(l)
while(len(qu)):
    print(qu)
    l=list(qu.pop(0))
    if(l==[1,1,1,1]):
        break
    l[0]=do(l[0])
    if(legal(l)):
        qu.append(tuple(l))
    for i in range(1,4):
        if(l[0]==l[i]):
            continue
        l[i]=do(l[i])
        if(legal(l)):
            p.append(l.copy())
            qu.append(tuple(l))
        l[i]=do(l[i])  
    

