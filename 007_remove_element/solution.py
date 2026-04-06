class Solution:
    def remove_element(self, nums: list[int], val: int) -> int:
        swap_index = len(nums) - 1
        index = 0
        while swap_index >= index:
            if nums[index] == val:  # swapperoo
                nums[swap_index], nums[index] = nums[index], nums[swap_index]
                swap_index -= 1
            else:
                index += 1
        return index


if __name__ == "__main__":
    s = Solution()

    nums = [3, 2, 2, 3]
    k = s.remove_element(nums, 3)
    assert k == 2
    assert nums[:k] == [2, 2]

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = s.remove_element(nums, 2)
    assert k == 5
    assert 2 not in nums[:k]
    assert sorted(nums[:k]) == sorted([0, 1, 3, 0, 4])

    print("Simple test cases passed!")
