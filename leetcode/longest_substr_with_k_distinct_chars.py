# Given a string, find the length of the longest substring in it with no more than K distinct characters.
## You can assume that K is less than or equal to the length of the given string.

def longestSubstringWithKdistinct(str, k):
    subStr = ''
    r = maxLen = 0
    
    while r < len(str):
        subStr += str[r]
        distinct_strs = set(subStr)
        if len(distinct_strs) > k:
            subStr = subStr[:-1]
            r -= 1

            maxLen = max(maxLen, len(subStr))

            subStr = subStr[1:]
        r += 1
    
    maxLen = max(maxLen, len(subStr))
    return maxLen

if __name__=="__main__":

    inputs = ["araaci", "araaci", "cbbebi", "abcdeffg", "aabacbebebe"]
    target_vals = [2, 1, 3, 3, 3]
    expected_outputs = [4, 2, 5, 4, 7]

    for i in range(len(expected_outputs)):
        assert longestSubstringWithKdistinct(inputs[i], target_vals[i]) == expected_outputs[i], f"Failed for ${i}"
    
    print("All test cases passed!")