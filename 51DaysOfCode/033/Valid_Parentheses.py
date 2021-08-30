class Solution:

    def is_match(self, p1: str, p2: str) -> bool:
        if p1 == '(' and p2 == ')':
            return True
        if p1 == '[' and p2 == ']':
            return True
        if p1 == '{' and p2 == '}':
            return True
        return False

    def isValid(self, s: str) -> bool:
        s1 = []
        is_balanced = True
        index = 0

        while index < len(s) and is_balanced:
            paran = s[index]

            if paran in "([{":
                s1.append(paran)
            else:
                if s1 == []:
                    is_balanced = False
                else:
                    top = s1.pop()
                    if not self.is_match(top, paran):
                        is_balanced = False
            index += 1

        if s == [] and is_balanced:
            return True
        else:
            return False

string = "(}"
print(Solution().isValid(string))