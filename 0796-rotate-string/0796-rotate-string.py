class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        r=s
        for i in range(len(s)):
            s=s[-1]+s[0:len(s)-1]
            if s==goal:
                return True
        return False        

        