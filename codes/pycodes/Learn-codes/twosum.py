import time
start_time=time.time()

def twoSum(nums, target):

        size=len(nums)
       
        for i in range(0,size):
                for j,num in enumerate(nums):

                    if(nums[i]+num == target and i!=j):
                        return [i,j]
                    

#list1=list(map(int,input("Enter values: ").split()))
#target=int(input("Enter target: "))

list1=[5,6,9,11,14]
target=20
print(twoSum(list1,target))
print(time.time()-start_time)