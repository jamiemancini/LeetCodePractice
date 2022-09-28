#1480. Running Sum of 1d Array

#Given an array nums. 
# #We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.

#Input: nums = [1,2,3,4]
#Output: [1,3,6,10]
#Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

def running_sum_fct(list):
    running_sum=[]
    running_sum.append(list[0])
    for i in range (1,len(list)):
        running_sum.append(running_sum[i-1]+list[i])
    return running_sum
    

nums = [1,2,3,4]

#test
print(running_sum_fct(nums))

#time complexity is O(N) because we go over every element in our input
#space complexity is O(1)
