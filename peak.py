a=[200,32,15,100,65]
n=5
print("Peak elements are")
for i in range(n):
    if((a[i-1]<a[i])and(a[i]>a[i+1])):
        print(a[i])
        break