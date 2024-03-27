import typing


class Solution:
    def remove_element(self, nums: typing.List[int], val: int) -> int:
        swap_index = len(nums) - 1
        index = 0
        while swap_index >= index:
            while nums[index] == val:  # swapperoo
                nums[swap_index], nums[index] = nums[index], nums[swap_index]
                swap_index -= 1
            index += 1
        return index, nums


if __name__ == "__main__":
    s = Solution()

    assert s.remove_element([3, 2, 2, 3], 3) == (2, [2, 2, 3, 3])
    assert s.remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2) == (5, [0, 1, 4, 0, 3, 2, 2, 2])

    print("Simple test cases passed!")
