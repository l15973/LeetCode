class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Example:
        # Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
        # Method 1 python內建方法
        intersectionR = set(nums1) & set(nums2)
        return list(intersectionR)

        # Method 2 
        intersectionR = set()

        for i in nums1:
            if i in nums2:
                intersectionR.add(i)
        return list(intersectionR)



test = Solution()
print(test.intersection([1, 2, 2, 1], [2,2]))