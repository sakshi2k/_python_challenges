def longestCommonPrefix(strs: list[str]) -> str:
    
    if "" in strs:
        return ""

    if len(strs) == 0:
        return ""
    
    prefix = strs[0]            # picking first word

    for i in range(1, len(strs)):           # iterating from second word onwards
        while strs[i].find(prefix) != 0:            # checking if prefix if present in chosen word
            prefix = prefix[0 : len(prefix) - 1]    # if not present, shorten prefix by removing one last character
            if prefix == "":                        
                return ""
    return prefix


if __name__ == "__main__":
    assert longestCommonPrefix(["flower","flow","flight"]) == "fl" 
    assert longestCommonPrefix(["dog","racecar","car"]) == ""
    assert longestCommonPrefix(["caravan","cartoon","car"]) == "car"
    assert longestCommonPrefix([""]) == ""
    assert longestCommonPrefix(["",""]) == ""
    assert longestCommonPrefix(["ab", "a"]) == "a"
    assert longestCommonPrefix(["flower","flower","flower","flower"]) == "flower"