import linked_list_utils


class Solution:
    def partition(
        self, head: linked_list_utils.LinkedListHead, x: int
    ) -> linked_list_utils.LinkedListHead:
        less_than_x_head = linked_list_utils.ListNode()
        greater_than_x_head = linked_list_utils.ListNode()

        less_than_x_tail = linked_list_utils.ListNode()
        greater_than_x_tail = linked_list_utils.ListNode()

        while head:
            if head.key < x:
                if less_than_x_tail.next is None:
                    less_than_x_head.next = head
                    less_than_x_tail = less_than_x_head.next
                else:
                    less_than_x_tail.next = head
                    less_than_x_tail = less_than_x_tail.next
            else:
                if greater_than_x_head.next is None:
                    greater_than_x_head.next = head
                    greater_than_x_tail = greater_than_x_head.next
                else:
                    greater_than_x_tail.next = head
                    greater_than_x_tail = greater_than_x_tail.next

            head = head.next

        # link the two lists together
        less_than_x_tail.next = greater_than_x_head.next

        # prevent a circular list
        greater_than_x_tail.next = None

        # handle an edge case of only the "greater than" list being used
        if less_than_x_head.next is None and greater_than_x_head.next is not None:
            return greater_than_x_head.next
        else:
            return less_than_x_head.next


if __name__ == "__main__":
    s = Solution()

    assert linked_list_utils.linked_list_to_list(
        s.partition(linked_list_utils.list_to_linked_list([1, 4, 3, 2, 5, 2]), 3)
    ) == [1, 2, 2, 4, 3, 5]
    assert linked_list_utils.linked_list_to_list(
        s.partition(linked_list_utils.list_to_linked_list([2, 1]), 2)
    ) == [1, 2]
    assert linked_list_utils.linked_list_to_list(
        s.partition(linked_list_utils.list_to_linked_list([1]), 0)
    ) == [1]

    print("Test cases passed!")
