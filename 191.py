def hammingWeight(self, n: int) -> int:
    sum = 0
    for num in str(n):
        if num == '1':
            sum = sum + 1
    return sum
