import heapq
s=input().split(' ')
d=set()
d2i={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'x':0}
k=0
for i in range(8):
    for j in range(i+1,9):
        if(s[i]=='x' or s[j]=='x'):
            continue
        if(d2i[s[i]]>d2i[s[j]]):
            k+=1
if(k%2):
    print(k)
    print('unsolvable')
    exit()
hp=[]
heapq.heappush(hp,(0,tuple(s),"",s.index('x')))
def f(y):
    t=y.index('x')
    return 2-t//3+2-t%3
while(len(hp)):
    g,tv,path,b=heapq.heappop(hp)
    x=list(tv)
    if(tv==('1','2','3','4','5','6','7','8','x')):
        print(path)
        exit()
    if(b-3>=0):
        x[b-3],x[b]=x[b],x[b-3]
        e=tuple(x)
        if(e not in d):
            d.add(e)
            heapq.heappush(hp,(g+f(e)+1,e,path+'u',b-3))
        x[b-3],x[b]=x[b],x[b-3]
    if(b%3!=0):
        x[b-1],x[b]=x[b],x[b-1]
        e=tuple(x)
        if(e not in d):
            d.add(e)
            heapq.heappush(hp,(g+f(e)+1,e,path+'l',b-1))
        x[b-1],x[b]=x[b],x[b-1]
    if(b%3!=2):
        x[b+1],x[b]=x[b],x[b+1]
        e=tuple(x)
        if(e not in d):
            d.add(e)
            d.add(e)
            heapq.heappush(hp,(g+f(e)+1,e,path+'r',b+1))
        x[b+1],x[b]=x[b],x[b+1]
    if(b+3<9):
        x[b+3],x[b]=x[b],x[b+3]
        e=tuple(x)
        if(e not in d):
            d.add(e)
            heapq.heappush(hp,(g+f(e)+1,e,path+'d',b+3))
        x[b+3],x[b]=x[b],x[b+3]
