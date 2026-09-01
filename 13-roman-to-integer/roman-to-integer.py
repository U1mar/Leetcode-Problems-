class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        num = 0
        x= 0
        while x < length:
            if s[x:x+2] == "IV":
                x+=1
                num += 4
            elif  s[x:x+2] == "IX" :
                x+=1
                num +=9
            elif s[x:x+2] == "XL":
                x+=1 
                num += 40
            elif s[x:x+2] == "XC":
                x +=1 
                num += 90
            elif s[x:x+2] =="CD":
                x +=1 
                num += 400
            elif s[x:x+2] =="CM":   
                x+=1 
                num +=900
            else:
                if s[x] == "I":
                    num += 1
                elif s[x] == "V":
                    num +=5 
                elif s [x] == "X":
                    num += 10 
                elif s[x] == "L" :
                    num +=50
                elif s[x]  == "C":
                    num +=100 
                elif s[x] == "D" :
                    num += 500 
                elif s[x] == "M" :
                    num +=1000
            x+=1
        return num 