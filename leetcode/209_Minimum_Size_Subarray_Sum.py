import sys
from datetime import datetime as dt

MAX_INT = sys.maxint if sys.version_info[0] < 3 else sys.maxsize

# __optimal approach
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
            r += 1
        
        return minCount if minCount != MAX_INT else 0


if __name__ == "__main__":
    s = Solution()
    # print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    
    inputs = [[2, 3, 1, 2, 4, 3], [1, 4, 4], [1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5]]
    target_vals = [7, 4, 11, 15]
    expected_outputs = [2, 1, 0, 5]

    for i in range(len(expected_outputs)):
        time_start = dt.now()
        assert s.minSubArrayLen(target_vals[i], inputs[i]) == expected_outputs[i], f"Failed for ${i}"
        time_end = dt.now()
        print(str(time_end - time_start))

    print("All test cases passed!")