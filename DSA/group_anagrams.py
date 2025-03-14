# 3. Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#     An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#     Constraints:
#         - 1 <= strs.length <= 104
#         - 0 <= strs[i].length <= 100
#         - strs[i] consists of lowercase English letters.
#     Example 1:
#         - Input: strs = ["eat","tea","tan","ate","nat","bat"]
#         - Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#     Example 2:
#         - Input: strs = [""]
#         - Output: [[""]]
#     Example 3:
#         - Input: strs = ["a"]
#         - Output: [["a"]]


from collections import defaultdict
from typing import List

def group_anagram (strings :List[str]) -> List[List[str]]:
    dict = defaultdict(list)

    for word in strings:
        sorted_word = sorted(word)
        key = tuple(sorted_word)
        
        if key not in dict:
            dict[key] = [word]
        else:
            dict[key].append(word)

        dict[key] = sorted(dict[key])
        

    return sorted(list(dict.values()),key=len)
    
print(group_anagram(["eat","tea","tan","ate","nat","bat"]))
print(group_anagram([""]))
print(group_anagram(["a"]))