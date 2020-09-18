"""将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<2:#为1时，根本不能实现变换
            return s
        res=[""for _ in range(numRows)]  #声明了一个长度为numRows的列表，每个元素都是一个空字符串。
        i,flag =0,-1
        for c in s:
            res[i] +=c    #python独有的字符加法
            if i==0 or i==numRows-1:
                flag=-flag#通过flag的转换实现在循环中反向填入内容
            i+=flag#
        return "".join(res)#join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。


A=Solution()
B='abcdefjhi'
C=3
D=A.convert(B,C)
print(D)

    
