#1672. Richest Customer Wealth

#You are given an m x n integer grid accounts where accounts[i][j] 
# is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
# Return the wealth that the richest customer has.

#A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.

#Input: accounts = [[1,5],[7,3],[3,5]]
#Output: 10

#Explanation: 
#1st customer has wealth = 6
#2nd customer has wealth = 10 
#3rd customer has wealth = 8
#The 2nd customer is the richest with a wealth of 10.

def find_richest(list):
    wealth=[]
    for i in range(len(list)):
        total=0
        for j in range(len(list[i])):
            total = total + list[i][j]
        wealth.append(total)
    wealthiest = 0
    for k in range(len(list)):
        if wealth[k] > wealthiest:
            wealthiest = wealth[k]
    return wealthiest

#Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
#Output: 17

accounts = [[2,8,7],[7,1,3],[1,9,5]]

print(find_richest(accounts))

#time complexity: 0(i*j) because it's proportional 
#to the sive of the list of lists
#space complexity: O(1) because we create a data structure
#proportional in size