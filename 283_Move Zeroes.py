class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
        
        # print(nums)
        # print(nums.count(0))
        count = nums.count(0)
        countZ = nums.count(0)
        while count !=0:
            zeroInd = nums.index(0)
            # print(zeroInd)
            # print(nums[:zeroInd])
            # print(nums[zeroInd+1:])
            if zeroInd ==0:
                nums[:len(nums)-1] = nums[1:]
                nums[-1] = 0
            else:
                nums[zeroInd:-1] = nums[zeroInd+1:]
                nums[-1] = 0 
                
            # print(nums)
            count -= 1
        print(nums)
        


test = Solution()

test.moveZeroes([0,1,0,3,12])
