c = []
v = []
lista = input().split()
lista = list(map(int, lista))
a, n =  lista[0], lista[1]

for i in range(n):
    listb = input().split()
    listb = list(map(int, listb))
    v.append(listb[0])
    c.append(listb[1])

def func(a, n):
    global c
    global v
    dp = [0 for i in range(a+1)]
 
    for i in range(1, n+1):
        for j in range(a, 0, -1): 
            if v[i-1] <= j:
                dp[j] = max(dp[j], dp[j-v[i-1]]+c[i-1])
    print(dp[a])

func(a, n)
