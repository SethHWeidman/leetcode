import typing


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: typing.Optional['TreeNode'] = None,
        right: typing.Optional['TreeNode'] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def bst_to_list(root: TreeNode) -> typing.List:
    # This function performs a level order traversal of the tree.
    # 'None' is used to represent the absence of a node in the level order traversal.

    if not root:
        return []

    result, queue = [], [root]
    while len(queue) > 0:
        current_level = []
        next_queue = []
        for node in queue:
            if node:
                current_level.append(node.val)
                next_queue.append(node.left)
                next_queue.append(node.right)
            else:
                current_level.append(None)

        # Append the current level to the result list
        result.extend(current_level)
        queue = next_queue

    # Trim the trailing 'None' values from the result list
    while result and result[-1] == None:
        result.pop()

    return result
