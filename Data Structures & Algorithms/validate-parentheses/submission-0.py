class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0,len(s)):
            if s[i] == "(" or s[i]=="{" or s[i]=="[":
                stack.append(s[i])
            else:
                if stack == []:
                    return False
                if stack[-1] == "(" and s[i] == ")":
                    stack.pop()
                elif stack[-1] == "[" and s[i] == "]":
                    stack.pop()
                elif stack[-1] == "{" and s[i] == "}":
                    stack.pop()
                else:
                    return False
        return stack == []
            


        