def lis(s):
    '''Esta es la documentacion'''
    assert len(s) == len([r for r in s if r >= 0])
    if len(s) == 0: return 0
    m = li(s)
    for i in range(len(s)):
        ns = list(s)
        ns.pop(i)
        n = lis(ns)
        m = max(m, n)
    return m

def li(s):
    a, m = -1, 0
    for i in s:
        if i > a: a,m = i, m+1
    return m

t = int(input())
l = []
while t != 0:
    input()
    s = map(int,input().split(' '))
    l.append(list(s))
    t -= 1
for s in l:
    print(lis(s))
