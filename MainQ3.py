number_cases = int(input())
def tkn(a,b):
    return str(a)+","+str(b)
for ___ in range(number_cases):
    frm = {}
    A,B = map(int,input().split())
    seen = set()
    queue = [(A,B)]
    frm[tkn(A,B)] = tkn(-1,-1)
    seen.add(tkn(A,B))
    qp = 0
    sv = -1
    while 1:
        a,b = queue[qp]
        if a==b:
            sv = a
            break
        qp+=1
        a1,b1 = a+1,b*2
        a2,b2 = a*2,b+1
        for an, bn in [(a1,b1), (a2,b2)]:
            if tkn(an,bn) not in seen:
                seen.add(tkn(an,bn))
                queue.append((an,bn))
                frm[tkn(an,bn)]=tkn(a,b)
    x = tkn(sv,sv)
    l = [x]
    while x!=tkn(A,B):
        x = frm[x]
        l = [x] + l
    print("  ".join(l))
            
