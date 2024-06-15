import typing


class Solution:
    def search(self, nums: typing.List[int], target: int) -> int:

        # low and high indices
        low, high = 0, len(nums) - 1

        # idea: if we split the array in half, at any given time, one of the arrays will be sorted.
        # we are going to "eliminate half the search space" on each binary search as follows:
        #   * we find one half is sorted and it does not contain `target` (in which case we
        #     eliminate it) OR
        #   * we find `target` in that half, in which case we eliminate the other half
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            # check if the left half is sorted
            if nums[low] <= nums[mid]:
                # left half is sorted
                if nums[low] <= target < nums[mid]:
                    # number is in left half
                    high = mid - 1
                else:
                    # number is not in right half
                    low = mid + 1
            else:
                # right half is sorted
                if nums[mid] < target <= nums[high]:
                    # number is in right half
                    low = mid + 1
                else:
                    # number is not in right half
                    high = mid - 1

        return -1


if __name__ == "__main__":
    s = Solution()

    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert s.search([1], 0) == -1

    assert s.search([5, 1, 3], 3) == 2
