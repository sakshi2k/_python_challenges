# Given a string, find the length of the longest substring in it with no more than K distinct characters.
## You can assume that K is less than or equal to the length of the given string.

def longestSubstringWithKdistinct(str, k):
    subStr = ''
    r = maxLen = distinct_strs = 0
    
    while r < len(str):
        if str[r] not in subStr:
            distinct_strs += 1
        subStr += str[r]

        while distinct_strs > k:
            removed_char = subStr[0]
            subStr = subStr[1:]
            if removed_char not in subStr:
                distinct_strs -= 1
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