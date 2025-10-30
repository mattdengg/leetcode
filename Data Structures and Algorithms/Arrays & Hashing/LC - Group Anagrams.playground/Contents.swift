/*
 49. Group Anagrams
 
 Given an array of strings strs, group the anagrams together. You can return the answer in any order.
 
 Example 1:

 Input: strs = ["eat","tea","tan","ate","nat","bat"]

 Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
 
 */


class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var res = [[Int]: [String]]()
        
        for s in strs {
            var count = Array(repeating: 0, count: 26)
            for c in s {
                count[Int(c.asciiValue!) - 97] += 1
            }
            res[count, default: []].append(s)
        }
        
        return Array(res.values)
    }
}

let solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


