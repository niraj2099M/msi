import time

g_time=[] #global list to store different exe times via decorator function

# problem statement : Find the count of elements whose value is greater than all of its previous elements in an array

def measure_execution_time(func): # how this nested func works? wrapper?
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        g_time.append(execution_time)
        print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        return result
    return wrapper



@measure_execution_time
def solve(A):
        lst=[]
        c=1
        for i in range(0,(len(A)-1)):
            lst.append(A[i])
            if (max(lst)< A[i+1]): #max finding max of lst in every iteration of i...max alsu using some form of iteration 
                c=c+1
        print(c)

@measure_execution_time
def solve_best(A):
        ans=1
        mx=A[0]
        for val in A[1:]:
            if (val>mx):
                ans+=1
                mx=val
        print(ans)

#test array
t=[]
for i in range(0,10000):
    t.append(i)

solve(t)
solve_best(t)     
print()

x=int(g_time[0]/g_time[1])
print("difference: ",x,"x")