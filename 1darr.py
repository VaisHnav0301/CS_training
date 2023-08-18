size=int(input("enter array size: "))
a=[]
m=[]
print("enter elements:")
for i in range(size):
    a.append(int(input()))
print("Entered array is: ",a)
count=0
for i in range(size):
        if a[i]!=0:
            a[count]=a[i]
            count+=1
while count<size:
    a[count]=0
    count += 1
print("Entered array is: ",a)