class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s.isalnum():
            charlist=list(s)
            charlist=[char.lower() for char in charlist if char.isalnum()]
            s="".join(charlist)
        else:
            s=s.lower()
        return s==s[::-1]        
