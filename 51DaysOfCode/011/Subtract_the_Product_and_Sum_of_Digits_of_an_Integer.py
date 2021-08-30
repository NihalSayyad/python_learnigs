'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
'''

class Solution:
    def subtractProductAndSum(self, n):
        sum, prod = 0,1
        while n:
            sum += (n%10)
            prod *= (n%10)
            n = (n/10)
        return prod - sum

print(Solution().subtractProductAndSum(123))