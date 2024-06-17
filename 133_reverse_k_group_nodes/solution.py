import linked_list_utils


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

    assert linked_list_utils.linked_list_to_list(
        s.reverse_k_group_nodes(linked_list_utils.list_to_linked_list([1, 2, 3, 4, 5]), 2)
    ) == [2, 1, 4, 3, 5]

    assert linked_list_utils.linked_list_to_list(
        s.reverse_k_group_nodes(linked_list_utils.list_to_linked_list([1, 2, 3, 4, 5]), 3)
    ) == [3, 2, 1, 4, 5]

    assert linked_list_utils.linked_list_to_list(
        s.reverse_k_group_nodes(linked_list_utils.list_to_linked_list([1, 2, 3, 4, 5]), 1)
    ) == [1, 2, 3, 4, 5]

    print("Test cases passed!")
