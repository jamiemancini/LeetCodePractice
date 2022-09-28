#Given an integer n, return a string array answer (1-indexed) where:

#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true.

#Example 1:

#Input: n = 3
#Output: ["1","2","Fizz"]

#Example 2:

#Input: n = 5
#Output: ["1","2","Fizz","4","Buzz"]

def fizz_buzz(int):
    list=[]
    for i in range(1,int+1):
        if i % 3 == 0 and i % 5 == 0:
            list.append(f"FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            list.append(f"Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            list.append(f"Buzz")
        else:
            list.append(f"{i}")
    return list

        

print(fizz_buzz(5))