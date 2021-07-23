
list=[1,2]

for i in range(3,101):
    n = 0
    for j in range(2,i):
        result = i%j
        if result ==0:
            break
        n=n+1
    if n==i-2:
        list.append(i)
print(list)

