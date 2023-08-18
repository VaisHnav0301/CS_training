row=int(input("enter rows"))
col=int(input("enter coloumns"))
m=[]
print("Enter elements")
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input()))
    m.append(a)
for i in range(row):
    for j in range(col):
        print(m[i][j],end=" ")
    print()
print("Diagonal elements:")
for i in range(row):
    for j in range(col):
        if i == j:
            print(m[i][j],end=" ")
        else:
            print(" ")
    print()
print("\nlower bound elements are:")
for i in range(row):
    for j in range(col):
        if i > j:
            print(m[i][j],end=" ")
print("\nupper bound elements are:")
for i in range(row):
    for j in range(col):
        if i < j:
            print(m[i][j],end=" ")