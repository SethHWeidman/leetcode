import typing


class Solution:
    def find_median_sorted_arrays(self, nums1: typing.List[int], nums2: typing.List[int]) -> float:
        # the idea for doing this efficiently (without loss of generality, assume `nums1` is the
        # shorter list):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # define `i := 0 <= i <= len(nums1)` and a corresponding `j` as a function of `i`, such
        # that at any given time:
        #
        #   if `len(nums1) + len(nums2)` is even, then taking `m := (len(nums1) + len(nums2)) / 2`,
        #   `len(nums1[:i]) + len(num2[:j]) == m`
        #
        #   if `len(nums1) + len(nums2)` is odd, then taking `m := (len(nums1) + len(nums2) + 1) //
        #   2`, `len(nums1[:i]) + len(num2[:j]) == m`
        #
        # Then, simply do binary search on `i`. Using the fact that `nums1` and `nums2` are both
        # sorted, we search until we find that the `m` lowest numbers are contained in a
        # combination of `nums[:i]` and `nums[:j]`; we can confirm this by checking:
        #
        #   `nums1[i - 1] <= nums2[j]` `nums2[j - 1] <= nums1[i]`
        #
        # When this is `True`, in the case when `len(nums1) + len(nums2)` is even, the median is
        # `(max(nums1[i - 1], nums2[j - 1]) + min(nums1[i], nums2[j])) / 2`, and when `len(nums1) +
        # len(nums2)` is odd, the median is `max(nums1[i - 1], nums2[j - 1])`
        m = len(nums1)
        n = len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2

        while True:
            i = (left + right) // 2
            j = half_len - i

            # should we decrease `i`?
            if i > 0 and nums1[i - 1] > nums2[j]:
                right = i - 1

            # should we increase `i`?
            elif i < m and nums2[j - 1] > nums1[i]:
                left = i + 1

            # `i` is in the right spot
            else:
                # work through the various edge cases, using the test cases below as guides
                if (m + n) % 2 == 0:
                    # everything in `nums1` is in the larger half
                    if i == 0:
                        max_of_left = nums2[j - 1]
                        if m > 0:
                            if j < n:
                                # normal case for `i == 0`
                                min_of_right = min(nums1[i], nums2[j])
                            else:
                                # edge case when `j == n`
                                min_of_right = nums1[i]
                        else:
                            # edge case
                            min_of_right = nums2[j]
                    # everything in `nums1` is in the smaller half
                    elif i == m:
                        if j > 0:
                            # normal case for `i == m`
                            max_of_left = max(nums1[i - 1], nums2[j - 1])
                        else:
                            # edge case when `j == 0`
                            max_of_left = nums1[i - 1]
                        min_of_right = nums2[j]
                    else:
                        # normal case
                        max_of_left = max(nums1[i - 1], nums2[j - 1])
                        min_of_right = min(nums1[i], nums2[j])

                    return (max_of_left + min_of_right) / 2.0

                else:
                    # case when the sum of the lists' lengths is odd is much easier
                    if i == 0:
                        return nums2[j - 1]
                    else:
                        return max(nums1[i - 1], nums2[j - 1])

        # will note for posterity that ChatGPT-4o suggested much cleaner branching logic after I
        # worked all this out:
        #
        # ```python
        # if i == 0:
        #     max_of_left = nums2[j - 1]
        # elif j == 0:
        #     max_of_left = nums1[i - 1]
        # else:
        #     max_of_left = max(nums1[i - 1], nums2[j - 1])
        #
        # if (m + n) % 2 == 1:
        #     return max_of_left
        #
        # if i == m:
        #     min_of_right = nums2[j]
        # elif j == n:
        #     min_of_right = nums1[i]
        # else:
        #     min_of_right = min(nums1[i], nums2[j])
        #
        # return (max_of_left + max_of_right) / 2.0
        # ```
        #
        # it is less obvious to me from inspection that this handles all edge cases properly, but
        # in testing, it appears to


if __name__ == "__main__":

    s = Solution()

    assert s.find_median_sorted_arrays([], [2, 3]) == 2.5

    assert s.find_median_sorted_arrays([3], [-2, -1]) == -1

    assert s.find_median_sorted_arrays([2], [1]) == 1.5

    assert s.find_median_sorted_arrays([1], [1]) == 1.0

    assert s.find_median_sorted_arrays([1, 3], [2]) == 2.0

    assert s.find_median_sorted_arrays([1, 2], [3, 4]) == 2.5

    print("All test cases passed!")
