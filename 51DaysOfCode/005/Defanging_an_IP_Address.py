
import re

class Solution:
    def defangIPaddr(self, address) :
        return re.sub('\.', '[.]', address)

address = '1.1.1.1'
print(Solution().defangIPaddr(address))