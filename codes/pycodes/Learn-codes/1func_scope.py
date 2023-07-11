

list_new=list(map(int,input("Enter numbers: ").split()))

def add(x):#simple list input
    j=0
    for i in x:
        j+=i
    return j

print("Sum= ",add(list_new))


def mul(x): #global var inside func
    global b
    b=1
    for i in x:
        b=b*i
    print("Product= ",b)
mul(list_new)

b=b-10  
print(b)


def f1(): #enclosed var
    t=5
    def f2(): 
        t=2
        s=t+b
        print(s)
        print("test: ",t)
        print(t-1000)
        
    f2()
    print(t)
f1()