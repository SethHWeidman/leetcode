import typing

import linked_list_utils


class Solution:
    def remove_nth_node_from_end(
        self, head: typing.Optional[linked_list_utils.ListNode], n: int
    ) -> typing.Optional[linked_list_utils.ListNode]:
        dummy = linked_list_utils.ListNode(0)
        dummy.next = head

        ahead = dummy
        behind = dummy

        for _ in range(n):
            ahead = ahead.next

        while ahead.next:
            ahead = ahead.next
            behind = behind.next

        behind.next = behind.next.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()

    assert linked_list_utils.linked_list_to_list(
        s.remove_nth_node_from_end(linked_list_utils.list_to_linked_list([1, 2, 3, 4, 5]), 2)
    ) == [1, 2, 3, 5]

    assert (
        linked_list_utils.linked_list_to_list(
            s.remove_nth_node_from_end(linked_list_utils.list_to_linked_list([1]), 1)
        )
        == []
    )

    assert linked_list_utils.linked_list_to_list(
        s.remove_nth_node_from_end(linked_list_utils.list_to_linked_list([1, 2]), 1)
    ) == [1]

    print("Simple test cases passed!")
