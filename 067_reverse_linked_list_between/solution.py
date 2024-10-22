import linked_list_utils
import typing


class Solution:
    def reverse_between(
        self, head: typing.Optional[linked_list_utils.ListNode], left: int, right: int
    ) -> typing.Optional[linked_list_utils.ListNode]:
        dummy = linked_list_utils.ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        start = prev.next
        then = start.next

        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        return dummy.next


if __name__ == "__main__":
    s = Solution()

    assert linked_list_utils.linked_list_to_list(
        s.reverse_between(linked_list_utils.list_to_linked_list([1, 2, 3, 4, 5]), 2, 4)
    ) == [1, 4, 3, 2, 5]

    assert linked_list_utils.linked_list_to_list(
        s.reverse_between(linked_list_utils.list_to_linked_list([5]), 1, 1)
    ) == [5]

    print("Simple test cases passed!")
