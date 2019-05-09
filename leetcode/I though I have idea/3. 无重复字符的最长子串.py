'''给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list(s)
        templine = []
        l = 0
        for i in s:
            if i in templine:
                templine.clear()
                templine.append(i)
            else:
                templine.append(i)
                if l >= len(templine):
                    pass
                elif l < len(templine):
                    l = len(templine)
        return l


if __name__ == '__main__':
    nums1 = "abcabcbb"
    nums2 = "bbbbb"
    nums3 = "pwwkew"
    error = "dvdf"
    a = Solution()
    p = a.lengthOfLongestSubstring(nums1)
    q = a.lengthOfLongestSubstring(nums2)
    r = a.lengthOfLongestSubstring(nums3)
    e = a.lengthOfLongestSubstring(error)
    print(p,q,r)
    print(e)