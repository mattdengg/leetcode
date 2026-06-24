#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'.
# Your task is to transform this absolute path into its simplified canonical path.
#
# The rules of a Unix-style file system are as follows:
#
# A single period '.' represents the current directory.
# A double period '..' represents the previous/parent directory.
# Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
# Any sequence of periods that does not match the rules above should be treated as a valid directory or file name.
# For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:
#
# The path must start with a single slash '/'.
# Directories within the path must be separated by exactly one slash '/'.
# The path must not end with a slash '/', unless it is the root directory.
# The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# Return the simplified canonical path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""

        for c in path + "/":
            if c == "/":
                if curr == "..":
                    if stack: stack.pop()           # go up one level (if possible)
                elif curr != "" and curr != ".":
                    stack.append(curr)              # valid name → push it
                curr = ""                           # reset for next segment

            else:
                curr += c                           # keep building the current name

        return "/" + "/".join(stack)

    # Time: O(n)
    # Space: O(n)

# @lc code=end