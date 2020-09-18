'''给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

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
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
'''
# 如果字符不在滑动窗口中，则直接扩展窗口
 # 如果字符在滑动窗口中，则
 # 1. 从窗口中移除重复字符及之前的字符串部分
 # 2. 再扩展窗口


  # 如果字符不在滑动窗口中，则直接扩展窗口
                # 右指针右移一位

            # 如果字符在滑动窗口中，则
            # 1. 从窗口中移除重复字符及之前的字符串部分
               # 在滑动窗口范围内中找出对应的首个字符的索引X，对应的新的左指针位置为X + 1  
            # 2. 再扩展窗口
               # 右指针右移一位

# 可抛弃字符串的索引尾值 - 字符串索引值，该索引值以及之前的字符都属于重复字符串中的一部分，不再在计算中涉及
    
       # 任意字符最后出现在索引的位置 - {字符: 字符索引值}

        for i, c in enumerate(s):
            # 如果字典中已经存在字符c，则字符c重复
            # 如果字符索引值大于ignore_str_index_end，则字符c在需处理的范围内（补充说明请参考备注一）
            if c in dic and dic[c] > ignore_str_index_end:
                # 先更新可抛弃字符串的索引尾值为字符c上一次的索引值
                ignore_str_index_end = dic[c]
                # 再更新字符c的索引值
                dic[c] = i
            # 否则，
            else:
                # 更新字符最近的索引位置
                dic[c] = i
                # 更新最大长度
                max_length = max(i - ignore_str_index_end, max_length)

        return max_length

作者：imckl
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/python-hua-dong-chuang-kou-xun-xu-jian-jin-de-3ge-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
                
           

作者：imckl
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/python-hua-dong-chuang-kou-xun-xu-jian-jin-de-3ge-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0#字符串为空警告
        lookup=list()#用来存窗口的信息
        n=len(s)
        max_len=0
        cur_len=0
        for i in range(n):
            val=s[i]#当前判断
            if not val in lookup:
                lookup.append(val)
                cur_len+=1
            else:
                index=lookup.index(val)
                lookup=lookup[index+1:]
                lookup.append(val)
                cur_len=len(lookup)
            if cur_len>max_len:
                max_len=cur_len
        return max_len

a=Solution()
try1='abccf'
k=a.lengthOfLongestSubstring(try1)
b=1