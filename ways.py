def dfs(start, depth):
    global res
    if depth > d:
        return
    if start == b:
        res += 1
        return
    used[start-1] = 1
    for i in range(n):
        if g[start-1][i] == 1 and used[i] == 0:
            dfs(i+1, depth+1)
    used[start-1] = 0

n, k, a, b, d = map(int, input().split())

g = [[0]*n for i in range(n)]
used = [0]*n

for i in range(k):
    a1, a2 = map(int, input().split())
    g[a1-1][a2-1] = 1

res = 0
def realization():
    global res
    dfs(a, 0)
    return res

print(realization())


            
    
    

    
