/*
 242. Valid Anagram
 
 Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 */

class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        s.sorted() == t.sorted()
    }
}

let solution = Solution()

print(solution.isAnagram("anagram", "nagaram"))
