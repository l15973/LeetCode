from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Example:
        # Given an array of size n, find the majority element. The majority element is the element that 
        # appears more than ⌊ n/2 ⌋ times.
        # You may assume that the array is non-empty and the majority element always exist in the array.

        # Method 1
        # a = Counter(nums).most_common()
        # if a[0][1] > len(nums)/2:
        #     return a[0][0] 
        # return None

        # Method 2
        for n in nums:
            


test = Solution()
print(test.majorityElement([3,1,3,3,5,3,8]))