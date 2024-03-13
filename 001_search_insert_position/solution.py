import typing


class Solution:
    def search_insert(self, nums: typing.List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # use `round` to ensure `pivot` is an `int`
            pivot = (left + right) // 2
            pivot_value = nums[pivot]
            if target == pivot_value:
                return pivot
            # search to the left by shifting `right` to the left, returning to the top of the
            # `while` loop
            elif target < pivot_value:
                right = pivot - 1
            # search to the right by shifting `left` to the right, returning to the top of the
            # `while` loop
            else:
                left = pivot + 1
        # if we have reached here, we have right < left (since `left <= right` is `False`). For
        # example, if `right` is 0 and `left` is 1, we want to place the element at 1, that is,
        # between the elements indicated by `right` and `left` test
        return left


if __name__ == "__main__":
    solution = Solution()

    assert solution.search_insert([1, 3, 5, 6], 5) == 2
    assert solution.search_insert([1, 3, 5, 6], 2) == 1
    assert solution.search_insert([1, 3, 5, 6], 7) == 4

    print("Simple test cases passed!")
