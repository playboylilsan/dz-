m , n = map(int,input().split()) # ну тут для любого варианта
data = [True] * 1001
k = 2
while k*k <= n:
    if data[k] == True:
        i = k*k
        while i<=n:
            data[i] = False
            i = i+k
    k += 1
for i in range(m,n):
    if data[i] == True: print(i)