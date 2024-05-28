import typing

import linked_list_utils


def create_linked_list(elements: typing.List[int]) -> linked_list_utils.LinkedListHead:
    """
    Function to create a linked list from a list of elements.
    :param elements: List[int] containing elements to be added to the linked list
    :return: The head of the linked list
    """
    if not elements:
        return None

    # Create the head of the linked list
    head = linked_list_utils.ListNode(elements[0])
    current = head

    # Iterate over the remaining elements and append them to the linked list
    for value in elements[1:]:
        current.next = linked_list_utils.ListNode(value)
        current = current.next

    return head


def linked_list_to_list(head: linked_list_utils.LinkedListHead) -> typing.List[int]:
    """
    Function to convert a linked list back to a Python list.
    :param head: ListNode representing the head of the linked list
    :return: List[int] containing the values from the linked list
    """
    result = []
    current = head
    while current:
        result.append(current.key)
        current = current.next
    return result


class Solution:
    def reverse_k_group_nodes(
        self, head: linked_list_utils.LinkedListHead, k: int
    ) -> linked_list_utils.LinkedListHead:
        if head is None:
            return None

        # count the number of nodes in the list
        num_nodes = 0
        temp_head = head
        while temp_head:
            num_nodes += 1
            temp_head = temp_head.next

        # idea: we will keep track of two key nodes at any given time:
        #   * `prev`, the node before the nodes we're reversing
        #   * `current`, which will be initialized to the node at the start of the group we're
        #     reversing
        #
        # first, we'll create a dummy node to initialize `prev`
        dummy = linked_list_utils.ListNode(-1)
        dummy.next = head
        prev, current = dummy, head

        next = head.next

        while k <= num_nodes:

            for _ in range(k - 1):
                # idea is to repeatedly "move `next` to in front of `prev`, and then shift
                # `current` down so that it points at a new `next` node
                # we need to perform `k - 1` swaps to reverse a group of size `k`
                current.next = next.next
                next.next = prev.next
                prev.next = next
                next = current.next

            # re-initialize variables for the next k-group reversal
            prev = current
            current = prev.next
            # the below handles the fact that, in thecase where `num_nodes` is a multiple of `k`,
            # `prev.next` will be `None`
            if current:
                next = current.next

            num_nodes -= k

        return dummy.next


if __name__ == "__main__":
    s = Solution()

    assert linked_list_to_list(
        s.reverse_k_group_nodes(create_linked_list([1, 2, 3, 4, 5]), 2)
    ) == [2, 1, 4, 3, 5]

    assert linked_list_to_list(
        s.reverse_k_group_nodes(create_linked_list([1, 2, 3, 4, 5]), 3)
    ) == [3, 2, 1, 4, 5]

    assert linked_list_to_list(
        s.reverse_k_group_nodes(create_linked_list([1, 2, 3, 4, 5]), 1)
    ) == [1, 2, 3, 4, 5]

    print("Test cases passed!")
