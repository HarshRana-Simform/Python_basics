from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for idx,val in enumerate(nums):

            if val-target in hashmap:
                return [idx,hashmap[val-target]]
            else:
                hashmap[val] = idx

        return 1

print(twoSum([2,7,11,15],9))