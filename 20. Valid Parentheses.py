"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'."""

class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        is_good = True
        for i in s:
            if i in "({[":
                stack.append(i)
            elif i in ")}]":
                if not stack:
                    return False        
                open_bracket = stack.pop()
                if open_bracket =="(" and i == ")":
                    continue
                if open_bracket =="{" and i == "}":
                    continue
                if open_bracket =="[" and i == "]":
                    continue
                is_good = False
                break
        if is_good and len(stack)==0:
            return True
        else:
            return False

if __name__ == "__main__":
    obj = Solution()
    s = input()
    result = obj.isValid(s)        
    print(result)