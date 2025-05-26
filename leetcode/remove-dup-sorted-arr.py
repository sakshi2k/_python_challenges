class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i < len(nums):
            # if curr element same as prev element
            if nums[i] == nums[i-1]:
                # remove current index
                nums.pop(i)
                # do not increment i because we need to check the new curr element at the same index
            else:
                # increment i
                i += 1
        
        return len(nums)
    

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # Output: 5