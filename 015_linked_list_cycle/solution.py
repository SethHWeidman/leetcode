import typing

import linked_list_utils


def create_linked_list_with_cycle(nodes: typing.List[int], pos: int) -> linked_list_utils.ListNode:
    if not nodes:
        return None

    head = linked_list_utils.ListNode(nodes[0])
    current = head
    nodes_map = {0: head}  # Map index to node

    for i in range(1, len(nodes)):
        current.next = linked_list_utils.ListNode(nodes[i])
        current = current.next
        nodes_map[i] = current

    if pos != -1:
        current.next = nodes_map[pos]  # Create cycle

    return head


class Solution:
    def has_cycle(self, head: typing.Optional[linked_list_utils.ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


if __name__ == "__main__":
    s = Solution()

    assert s.has_cycle(create_linked_list_with_cycle([3, 2, 0, -4], 1))
    assert s.has_cycle(create_linked_list_with_cycle([1, 2], 0))
    assert not s.has_cycle(create_linked_list_with_cycle([1], -1))
    assert not s.has_cycle(create_linked_list_with_cycle([], -1))

    print("All test cases passed!")
