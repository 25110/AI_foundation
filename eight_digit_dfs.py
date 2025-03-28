s=input().split(' ')
d=set()
def dfs(b,x):
    v=tuple(s)
    if(v in d): 
        return
    if(x>100):
        return
    if(v==('1','2','3','4','5','6','7','8','x')):
        print(1)
        exit()
    d.add(v)
    if(b-3>=0):
        s[b-3],s[b]=s[b],s[b-3]
        dfs(b-3,x+1)
        s[b-3],s[b]=s[b],s[b-3]
    if(b%3!=0):
        s[b-1],s[b]=s[b],s[b-1]
        dfs(b-1,x+1)
        s[b-1],s[b]=s[b],s[b-1]
    if(b%3!=2):
        s[b+1],s[b]=s[b],s[b+1]
        dfs(b+1,x+1)
        s[b+1],s[b]=s[b],s[b+1]
    if(b+3<9):
        s[b+3],s[b]=s[b],s[b+3]
        dfs(b+3,x+1)
        s[b+3],s[b]=s[b],s[b+3]
    d.remove(v)
for i in range(9):
    if(s[i]=='x'):
        p=i
        break
dfs(p,1)
print(0)