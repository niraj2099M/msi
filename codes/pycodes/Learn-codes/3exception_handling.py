a=int(input("Enter a number: "))


if(a>5):
    try:
        b=a/0
    except Exception as e:
        print(e)
    print("Greater then 5")
else:
    print(a)



"""In math there are rules about dividing by zero. The below code is trying to do just that and will throw a ZeroDivisionError. 
Add exception handling to return back 0 instead of allowing the error to be thrown."""

def divide_by(a, b)
    try:
        return a / b
    except:
        return 0


ans = divide_by(40, 0)
print(ans)


"""The below code has one problem. It is trying to locate an item from the list that does not exist. 
Running the code will throw the IndexError. Add exception handling to stop the error from being thrown and return a more user-friendly message such
 as "Item does not exist in the list"."""

items = [1,2,3,4,5]
try:
    item = items[6]
    print(item)
except:
    print("Item does not exist in the list")