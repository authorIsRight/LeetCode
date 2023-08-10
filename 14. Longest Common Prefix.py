"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters."""

import json
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        suffix = ""
        for i in zip(*strs):
            if len(set(i)) == 1: 
                print(i)
                suffix += i[0]
            else: 
                return suffix
        return suffix

def read_input():

    strs = json.loads(input())

    return strs


if __name__ == "__main__":
    strs = read_input()
    obj = Solution()
    to_print = obj.longestCommonPrefix(strs)
    print(to_print)
