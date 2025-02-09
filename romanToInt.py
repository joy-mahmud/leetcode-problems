numlist={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
class Solution:
    
    def romanToInt(self, s: str) -> int:
        sum = 0
        x=0
        while x < len(s):
            if x != len(s)-1:
                if numlist[s[x]]< numlist[s[x+1]]:
                    res= numlist[s[x+1]]-numlist[s[x]]
                    sum = sum+res 
                    x=x+2
                    continue
        
            sum = sum+numlist[s[x]]
            x=x+1
        return sum    

obj = Solution()
print(obj.romanToInt('LVIII'))
# print(numlist["I"])
        
        