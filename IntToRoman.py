class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s=''
        roman=['I','V','X','L','C','D','M']
        integer=[1,5,10,50,100,500,1000]
        #roman_val={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=len(integer)-1
        while True:
            div=integer[i]
            if num>div:
                qu=num//div
                s+=roman[i]*qu
                rem=num%div
                num=rem

            if num<=0:
                break
        return s

obj=Solution()
print(obj.intToRoman(4567))
