class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        flag = False
        x = 0
        point =[]
        while not flag and x< len:
            for y in range (length):
                if x != y and nums[x] + nums[y] == target:
                    flag = True 
                    point = [x,y]
                    break
            x+=1

        return point