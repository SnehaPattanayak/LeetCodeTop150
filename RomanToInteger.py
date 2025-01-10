class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        integer=0
        n=len(s)
        roman_val={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)):
            if i<n-1 and roman_val[s[i]]<roman_val[s[i+1]]:
                integer-=roman_val[s[i]]
            else:
                integer+=roman_val[s[i]]
        return integer
