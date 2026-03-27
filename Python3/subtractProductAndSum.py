class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        prod = 1
        while n != 0:
            summ += n % 10
            prod *= n % 10
            n //= 10
        return prod - summ
