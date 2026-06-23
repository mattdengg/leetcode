/*
 1. Two Sum

 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

 You may assume that each input would have exactly one solution, and you may not use the same element twice.

 You can return the answer in any order.
 */

class Solution {
    func twoSum(_ nums: [Int],_ target: Int) -> [Int] {
        var prevMap = [Int: Int]()
        
        for (i,n) in nums.enumerated() {
            let diff = target - n
            if let index = prevMap[diff] {
                return [index, i ]
            }
            prevMap[n] = i
        }
        return []
    }
}

let solution = Solution()

print(solution.twoSum([2,7,11,15], 9))
