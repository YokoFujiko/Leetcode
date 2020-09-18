class Solution(object):
    def lengthOfLongestSubstring(self, s: str):

        if not s:
            return 0
        max_length = 0      # 滑动窗口数组
        left, right = 0, 0  # 双指针

        for i, c in enumerate(s):
            # 如果字符不在滑动窗口中，则直接扩展窗口
            if c not in s[left:right]:
                # 右指针右移一位
                right += 1
            # 如果字符在滑动窗口中，则
            # 1. 从窗口中移除重复字符及之前的字符串部分
            # 2. 再扩展窗口
            else:
                # 在滑动窗口范围内中找出对应的首个字符的索引X，对应的新的左指针位置为X + 1
                # 左指针右移 索引X增一 位
                left += s[left:right].index(c) + 1
                # 右指针右移一位
                right += 1

            # 更新最大长度
            max_length = max(right - left, max_length)

        # 如果最大长度不为零，返回最大长度
        # 如果最大长度仍为零，则说明遍历整个字符串都没有发现重复字符，最大长度即为字符串本身的长度
        return max_length if max_length != 0 else len(s)
