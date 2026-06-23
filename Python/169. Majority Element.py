#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
#
# Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
# Example 1:
# Input: nums = [3, 2, 3]
# Output: 3
#
# Example 2:
# Input: nums = [2, 2, 1, 1, 1, 2, 2]
# Output: 2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        max_count = -1
        ans = -1

        for key, val in counter.items():
            if val > max_count:
                max_count = val
                ans = key

        return ans

    # Time: O(n)
        # Space: O(n)


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        ans = -1
        count = 0

        for num in nums:
            if count == 0:
                ans = num

            if ans == num:
                count += 1
            else:
                count -= 1

        return ans

    # Time: O(n)
    # Space: O(1)

# @lc code=end