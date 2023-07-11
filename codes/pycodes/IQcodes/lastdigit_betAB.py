import time
# problem statement : Find the number of integers in range [A, B] with last digit C.

g_time=[]
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
def solve_brute(A, B, C):
    #l=u=0
    s=0
    for i in range(A,B+1):
        if i%10==C:
            s+=1
    return(s)
    
@measure_execution_time
def solve_op(A,B,C):

    for i in range(A,B+1):
        if i%10==C: 
            l=i
            break;


    for i in range(B,A-1,-1):
        if i%10==C: 
            u=i
            break;     

    s=0
    if(B-A)<10:
        for i in range(A,B+1): #edge case as bottom eqn when range <10 if no number still adding 1 as per eqn
            if i%10==C:
                s=1
        return(s)
    else:
        s=((u-l)/10)+1  #came at this equation while working on white board but didnt consider edge case possibility
        return(int(s))
    

a=solve_brute(1223,123987,2)
b=solve_op(1223,123987,2)
print(a, b)

x=int(g_time[0]/g_time[1])
print("difference: ",x,"x")