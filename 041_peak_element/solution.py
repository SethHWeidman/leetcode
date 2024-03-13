import typing


class Solution:
    def find_peak_element(self, nums: typing.List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:

            mid = int((left + right) / 2)
            # we are on an "upward slope"
            if nums[mid] < nums[mid + 1]:
                # peak must be to the right; since `mid` is less than the element to the right, we
                # want to eliminate it from the search
                left = mid + 1

            # we are on a "downward slope"
            else:
                # peak must be to the left
                right = mid
        return right
