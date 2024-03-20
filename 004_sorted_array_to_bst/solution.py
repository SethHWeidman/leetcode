import typing

from leetcode import tree_utils


class Solution:
    def sorted_array_to_bst(self, nums: typing.List[int]) -> typing.Optional[tree_utils.TreeNode]:
        # the key here is to draw things out and realize that selecting the middle element (by
        # index) at each step of the recursion will result in a tree that is height-balanced
        if len(nums) == 0:
            return None
        mid_index = len(nums) // 2
        head = tree_utils.TreeNode(nums[mid_index])

        # note that because of the way Python indexes lists, this will not include `mid_index`
        head.left = self.sorted_array_to_bst(nums[0:mid_index])

        # for the second index: we need to pass in `len(nums)` instead of `len(nums) - 1` since we
        # are taking slices of the list, and if `L` is a list, L[0:len(L) - 1] will miss the last
        # element (this tripped me up initially)
        head.right = self.sorted_array_to_bst(nums[mid_index + 1 : len(nums)])
        return head


if __name__ == "__main__":
    s = Solution()

    assert tree_utils.bst_to_list(s.sorted_array_to_bst([-10, -3, 0, 5, 9])) == [
        0,
        -3,
        9,
        -10,
        None,
        5,
    ]
    assert tree_utils.bst_to_list(s.sorted_array_to_bst([1, 3])) == [3, 1]
