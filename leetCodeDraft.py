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
points = [[2,3]]
print(nearestValidPoint(3,4,points))

