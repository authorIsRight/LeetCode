"""9. Palindrome Number
Easy
10.5K
2.6K
Companies
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        origin_x = x
        back_x = 0

        if x < 0:
            return False

        while x > 0:
            back_x = back_x*10 + x % 10
            x = x//10

        return back_x == origin_x


def read_input():
    palindrom = input()
    return palindrom


if __name__ == "__main__":
    x = int(read_input())
    solution = Solution()
    print(solution.isPalindrome(x))
