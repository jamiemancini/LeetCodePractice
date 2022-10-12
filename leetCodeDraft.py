def largestPerimeter(nums):
        nums.sort()
        print(nums)
        perimeter = 0
        n=0
        while n < len(nums)-2:
            if nums[len(nums)-3-n] + nums[len(nums)-2-n] > nums[len(nums)-1-n]:
                perimeter = nums[len(nums)-3-n] + nums[len(nums)-2-n ] + nums[len(nums)-n-1]
            n +=1
            print(f" n is: {n}")
            print(f"perimeter is {perimeter}")
        return perimeter

def nearestValidPoint(x,y,points):
    i = 0
    manDist=float('inf')

    for list in points:
        
        if list[0]==x or list[1]==y:
            print("match made")
            calcDist = abs(list[0]-x) + abs(list[1]-y)
            if calcDist < manDist:
                manDist = calcDist
                index = i
            print(f"the index is {index}")
            print(f"the manDist is {manDist}")
        i += 1
    
    if manDist==float('inf'):
        print("here")
        return -1
    else:
        return index

#points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
#points = [[2,3]]
#print(nearestValidPoint(3,4,points))

def isHappy(n):
    #while the length of n is more than 1 digit
    if n < 10:
        n=n**2
    while len(str(n))> 1:
        #loop through to find the sum of all digits squared
        result=0 #after the for loop DONT forget to set result = 0
        for digit in str(n):
            result = result + (int(digit))**2
        n=result
        print(n)    
    if n==1:
        return True
    else:
        return False

def isHappy2(n):
    #create a set so that you can check what values you've visited
    #because if you visit a value again then you'll be caught in an infinite loop
    seen = set()
    while n not in seen:
        seen.add(n)
        result=0 #after the for loop DONT forget to set result = 0
        for digit in str(n):
            result = result + (int(digit))**2
            n=result
        print(n)    
        if n==1:
            return True
    return False

#print(isHappy2(1111111))
def areAlmostEqual(s1,s2):
    if s1==s2:
        return True
    elif len(s1)!= len(s2):
        return False
    i=0
    countDifferences=0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            countDifferences += 1
    if countDifferences == 2:
        return True
    else:
        return False
    
print(areAlmostEqual("ballws", "kawnbs"))



