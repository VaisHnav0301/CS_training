print("welcome....")
print("select your drink and pay...")
cap=200
stk=10
a=int(input("how many pepsi bottles you want ?:"))
if stk>=a:
    for i in range(a):
        print("TAKE IT-:)")
else:
    for j in range(stk):
        print("TAKE IT-:)")

    print("Available bottles of pepsi is: ",stk)
    print("OUT OF STOCK")
print("ENJOY YOUR DRINK ^_^")
