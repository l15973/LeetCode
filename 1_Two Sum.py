# Two Sum
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
import collections
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        twosumDict = collections.defaultdict(int)
        for ind in range(len(nums)):
            for anotherInd in range(ind+1, len(nums)):                
                if nums[ind] + nums[anotherInd] == target:
                    return ([ind, anotherInd])
        #         twosumDict[(ind, anotherInd)] = nums[ind] + nums[anotherInd]
                
        # print(twosumDict)
        # for key, value in twosumDict.items():
        #     if value == target:
        #         return list(key)
test = Solution()
print(test.twoSum( [2, 7, 11, 15], 9))       