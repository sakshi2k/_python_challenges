import sys

MAX_INT = sys.maxint if sys.version_info[0] < 3 else sys.maxsize

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minCount = MAX_INT
        l = r = currSum = 0

        while r < len(nums):
            currSum += nums[r]
            while currSum >= target:
                count = r - l + 1
                minCount = min(count, minCount)
                currSum -= nums[l]
                l += 1
                # r = l
            r += 1
        
        return minCount if minCount != MAX_INT else 0


if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))