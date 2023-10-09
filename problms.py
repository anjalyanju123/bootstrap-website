num=[2,4,5]
n=len(num)
target=6
for i in range(n):
    for j in range(0,n):
        if (num[i]+num[j]==target):
            print([i,j]) 
            break