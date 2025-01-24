import typing

import tree_utils


class BSTIterator:
    def __init__(self, root: tree_utils.TreeNode):
        self.stack = []
        self._add_left_to_stack(root)

    def _add_left_to_stack(self, root: tree_utils.TreeNode) -> None:
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        last_node = self.stack.pop()

        if last_node.right:
            self._add_left_to_stack(last_node.right)

        return last_node.val

    def has_next(self) -> bool:
        return len(self.stack) > 0


def test_bst_iterator(bst_iterator: BSTIterator, method_calls: typing.List[str]):
    """
    Helper function to test BSTIterator by executing a sequence of method calls and returning their
    outputs.

    Args:
        bst_iterator: An instance of BSTIterator to test
        method_calls: List of method names to call ('next' or 'has_next')

    Returns:
        List of outputs from executing the method calls in sequence
    """
    outputs = []

    for method in method_calls:
        if method == "next":
            outputs.append(bst_iterator.next())
        elif method == "has_next":
            outputs.append(bst_iterator.has_next())

    return outputs


if __name__ == "__main__":

    assert test_bst_iterator(
        BSTIterator(tree_utils.list_to_tree([7, 3, 15, None, None, 9, 20])),
        ["next", "next", "has_next", "next", "has_next", "next", "has_next", "next", "has_next"],
    ) == [3, 7, True, 9, True, 15, True, 20, False]
