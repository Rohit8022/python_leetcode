class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        c=0
        g.sort()
        s.sort()
        i,j=0,0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                c+=1
            
                i+=1
                
            j+=1    
        return c        




        