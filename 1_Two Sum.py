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
        # Method 1 時間複雜度是O(n^2)
        # twosumDict = collections.defaultdict(int)
        # for ind in range(len(nums)):
        #     for anotherInd in range(ind+1, len(nums)):                
        #         if nums[ind] + nums[anotherInd] == target:
        #             return ([ind, anotherInd])
        
        # Method 2 時間複雜度O(n)
        valIndexDict = collections.defaultdict(int)
        for i in range(len(nums)):
            current = nums[i]
            if target - current in valIndexDict:
                return [valIndexDict[target-current], i]
            valIndexDict[current] = i
test = Solution()
# print(test.twoSum( [2, 7, 11, 15], 9))
print(test.twoSum( [0,1,2,0], 0))       