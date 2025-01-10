class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=list(s.strip().split())
        return len(s[-1])

        
