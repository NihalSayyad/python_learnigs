from stack import Stack

def is_match(p1, p2):
    if p1 == "[" and p2 == "]":
        return True
    if p1 == "(" and p2 == ")":
        return True
    if p1 == "{" and p2 == "}":
        return True

def if_paran_balanced(paran_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paran_string) and is_balanced:
        paran = paran_string[index]
        if paran in "([{":
            s.push(paran)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paran):
                    is_balanced = False
        index +=1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


class Solution:

    def is_match(self, p1, p2) :
        if p1 == '(' and p2 == ')':
            return True
        if p1 == '[' and p2 == ']':
            return True
        if p1 == '{' and p2 == '}':
            return True

    def isValid(self, s) :
        s = []
        is_balanced = True
        index = 0

        while index < len(s) and is_balanced:
            paran = s[index]

            if paran in "([{":
                s.append(paran)
            else:
                if s == []:
                    is_balanced = False
                else:
                    top = s.pop()
                    if not self.is_match(top, paran):
                        is_balanced = False
            index += 1

        if s == [] and is_balanced:
            return True
        else:
            return False

string = "{[()]}"

Solution().isValid(string)


string = "[{()"
print(if_paran_balanced(string))