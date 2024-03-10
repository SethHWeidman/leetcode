import typing

class Solution:
    def majority_element(self, nums: typing.List[int]) -> int:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            else:
                counter[num] += 1
        # an equivalent way to produce `counter` would be
        # 
        #     import collections
        #     counter = collections.Counter(nums)        

        return max(counter.keys(), key=counter.get)
    

if __name__ == '__main__':
    solution = Solution()

    assert solution.majority_element([3,2,3]) == 3
    assert solution.majority_element([2,2,1,1,1,2,2]) == 2