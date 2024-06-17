import typing


class ListNode:
    def __init__(self, key: int = -1, val: int = -1):
        self.key = key
        self.val = val
        self.next: ListNode = None
        self.prev: ListNode = None


LinkedListHead = typing.Optional[ListNode]


def linked_list_to_list(head: LinkedListHead) -> typing.List[int]:
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


def list_to_linked_list(elements: typing.List[int]) -> LinkedListHead:
    """
    Function to create a linked list from a list of elements.
    :param elements: List[int] containing elements to be added to the linked list
    :return: The head of the linked list
    """
    if not elements:
        return None

    # Create the head of the linked list
    head = ListNode(elements[0])
    current = head

    # Iterate over the remaining elements and append them to the linked list
    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next

    return head
