class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        length = len(str(x))
        Flag = True
        string = str(x)
        i = 0
        for i in range (length // 2):
            if string[i] != string[length -1 -i]:
                Flag = False
                break
        return Flag