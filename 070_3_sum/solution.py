import typing


class Solution:
    def three_sum(self, nums: typing.List[int]) -> typing.List[typing.List[int]]:
        if not len(nums):
            return []

        answer = []
        nums.sort()
        N = len(nums)

        for i in range(N - 2):
            # if we just checked for triplets starting with this number, skip
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left = i + 1
            right = N - 1

            while left < right:
                proposed = nums[i] + nums[left] + nums[right]

                if proposed == 0:
                    answer.append([nums[i], nums[left], nums[right]])

                    # skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # skip duplicates for the right pointer
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1

                    left += 1
                    right -= 1

                # too big
                elif proposed > 0:
                    right -= 1

                # too small
                else:
                    left += 1

        return answer


if __name__ == "__main__":
    s = Solution()

    assert s.three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert s.three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert s.three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
    assert s.three_sum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]

    print("Test cases passed!")
