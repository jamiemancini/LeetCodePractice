
def countOdds(low, high):
    if low == high:
        if low % 2 == 0:
            return 0
        else:
            return 1
    elif low % 2 == 0 and high % 2 == 0:
        count= (high - low)//2
    elif low % 2 == 0 and high % 2 != 0:
        count = (high-low + 1)//2
    elif low % 2 != 0 and high % 2 != 0:
        count = (high - low)//2 + 1
    else:
        count = (high -low + 1) // 2
    return count

print(countOdds(11,21))

#Python 1 line solution:
#class Solution:
#def countOdds(self, low: int, high: int) -> int:
#return 1+(high-low)//2 if high%2 or low%2 else (high-low)//2

def modus(high):
    return ("hello") if high%2 else print("goodbye")

print(modus(9))