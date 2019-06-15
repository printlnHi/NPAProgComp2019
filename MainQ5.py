TCN = int(input())
def apply(mp, re, ce, rn, cn):
    #1-indexed coordinates
    nm = list(mp)
    for i in range(re-1,rn):
        nm[i] = min(nm[i],ce-1)
    return nm

def pr(mp,rn,cn):
    print("@"+"#"*(mp[0]-1))
    for x in mp[1:]:
        if x:
            print("#"*x)
    
    

def p1(mp,rn,cn):
    return rn>=3 and mp[0]==2 and mp[1]==2 and mp[2]==1 and sum(mp[3:])==0

def p2(mp,rn,cn):
    return rn>=2 and mp[0]==3 and mp[1]==2 and sum(mp[2:])==0

def p3(mp,rn,cn):
    return rn>=3 and mp[0:3] == [4,2,2] and sum(mp[3:])==0

def p4(mp, rn, cn):
    return rn>=4 and mp[0:4] == [3,3,1,1] and sum(mp[4:])==0

def is_losing(mp,rn,cn):
    if mp[0]==1+sum(mp[1:]) and max(mp[1:])<=1:
        return True
    return p1(mp,rn,cn) or p2(mp,rn,cn) or p3(mp,rn,cn) or p4(mp,rn,cn)

def make_losing(mp,rn,cn):
    for xr in range(1,rn+1):
        for xc in range(1,mp[xr-1]+1):
            x = apply(mp,xr,xc,rn,cn)
            if is_losing(x,rn,cn):
                return (xr,xc)
    return None

    return None

for ___  in range(TCN):
    if ___ !=0:
        print()
    RN, CN = map(int,input().split())
    obj = [int(CN) for i in range(RN)]
    pr(obj,RN,CN)
    print()
    while 1:
        #Player A move
        if is_losing(obj,RN,CN):
            print("A eats (1,1):\nPlayer A loses.")
            break
        los = make_losing(obj,RN,CN)
        if los:
            print("A eats (%d,%d):"%(los[0],los[1]))
            obj = apply(obj,los[0],los[1],RN,CN)
            pr(obj,RN,CN)
            print()
        else:
            etr = RN-1
            while (etr>0 and obj[etr]<2):
                etr-=1
            etc = obj[etr]
            print("A eats(%d,%d):"%(etr+1,etc))
            obj = apply(obj,etr+1,etc,RN,CN)
            pr(obj,RN,CN)
            print()
        #Player B move
        if is_losing(obj,RN,CN):
            print("B eats (1,1):\nPlayer B loses.")
            break
        los = make_losing(obj,RN,CN)
        if los:
            print("B eats (%d,%d):"%(los[0],los[1]))
            obj = apply(obj,los[0],los[1],RN,CN)
            pr(obj,RN,CN)
            print()
        else:
            if obj[1]!=0:
                etr = 2
                etc = obj[1]
            else:
                etr = 1
                etc = obj[0]
            print("B eats (%d,%d):"%(etr,etc))
            obj = apply(obj,etr,etc,RN,CN)
            pr(obj,RN,CN)
            print()
        
        
