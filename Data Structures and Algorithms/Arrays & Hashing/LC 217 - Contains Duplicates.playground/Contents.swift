/*
 217. Contains Duplicate
 
 Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 */

class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        return Set(nums).count != nums.count
    }
}

let solution = Solution()

print(solution.containsDuplicate([1, 2, 3, 1]))
print(solution.containsDuplicate([1, 2, 3, 4]))
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
