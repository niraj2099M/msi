import time


# bruteA and optimized both count the number of sundays given A= 1st day of month (string: ef "Monday")
# and B= no of days in that month, 1<= B <= 10^9

def measure_execution_time(func): # how this nested func works? wrapper?
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        return result
    return wrapper
   

@measure_execution_time # m1. Use decorators
def bruteA(A, B):
        
    day=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    sun=0
    for i,d in enumerate(day): #dict implentation via loop >> not good for big data size
        if d==A:
            c=i+1
            
    while B>0:   #looping over large numbers significantly increases execution time
        if c%7 ==0:
            sun=sun+1
        c=c+1
        B=B-1
    return sun

@measure_execution_time
def optimized(A, B):
        
    day=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    sun=0
    for i,d in enumerate(day):
        if d==A:
            c=i

    B=B+c
    B//=7
    return B



# m2. Use these to test time taken by any part of code esp calling funs and methods from outside the code file
"""
start_time = time.time()

<<Codes to be speed tested>

end_time = time.time()

execution_time = end_time - start_time

print("Execution time:", execution_time, "seconds")
"""


print(bruteA("Monday", 500000))
print("looping over large number is slow, try to find some other way>> algos or some way to do without looping","\n")
print(optimized("Monday",500000))


