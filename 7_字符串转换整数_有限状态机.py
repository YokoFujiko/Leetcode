INT_MAX=2**31-1
INT_MIN=-2**31

class Automaton:
    def __init__(self):
        self.state="start"#状态初始化为start
        self.ans=0
        self.sign=1
        self.table = { "start":["start", "signed","number","end"],
                       "signed":["end","end","number","end"],
                       "number":["end","end","number","end"],
                       "end":["end","end","end","end"] }
    def get_str(self,c):
        """获取当前字符，判断转到哪一个状态"""
        if c.isspace():
            return 0
        elif c=="+" or c=="-":
            return 1
        elif c.isdigit():
            return 2
        else:
            return 3
    def state_jump(self,c):
        self.state=self.table[self.state][self.get_str(c)]
        if self.state=="number":
            self.ans=self.ans*10+int(c)
        if self.state=="signed" and c=="-":
            self.sign=-1
    

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        automaton=Automaton()
        i=len(str)
        if i==0:
            return 0
        else:
            for c in str:
                i=i-1
                automaton.state_jump(c)
                if automaton.state=="end" or i==0:
                    if automaton.sign == 1:
                        return min(INT_MAX,automaton.ans*automaton.sign)
                    else:
                        return max(INT_MIN,automaton.ans*automaton.sign)


test=""
s=Solution()
c=s.myAtoi(test)
print(c)
            
