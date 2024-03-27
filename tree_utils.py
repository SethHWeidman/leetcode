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


def list_to_tree(elements: typing.List[typing.Optional[int]]) -> typing.Optional[TreeNode]:
    if not elements:
        return None  # No elements to convert into a tree

    # First element of the list is the root
    root = TreeNode(elements[0])
    # Queue for level order tree construction, containing pairs of (TreeNode, Index in 'elements')
    queue = [(root, 0)]

    while queue:
        node, idx = queue.pop(0)
        left_idx = 2 * idx + 1  # Index of left child in the list
        right_idx = 2 * idx + 2  # Index of right child in the list

        # If there is a left child, add it to the node and queue
        if left_idx < len(elements) and elements[left_idx] is not None:
            node.left = TreeNode(elements[left_idx])
            queue.append((node.left, left_idx))

        # If there is a right child, add it to the node and queue
        if right_idx < len(elements) and elements[right_idx] is not None:
            node.right = TreeNode(elements[right_idx])
            queue.append((node.right, right_idx))

    return root
