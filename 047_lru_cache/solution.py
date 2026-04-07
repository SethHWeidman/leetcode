import linked_list_utils


def run_lru_cache(commands: list, arguments: list) -> list:
    results = []
    lru_cache = None

    for command, args in zip(commands, arguments):
        if command == "LRUCache":
            lru_cache = LRUCache(*args)
            results.append(None)
        elif command == "put":
            lru_cache.put(*args)
            results.append(None)
        elif command == "get":
            result = lru_cache.get(*args)
            results.append(result)

    return results


class LRUCache:
    """
    LRU Cache using a doubly-linked list + hashmap.

    The list maintains access order. The "tail" end holds the most recently
    used (MRU) items, and the "head" end holds the least recently used (LRU).
    """

    def __init__(self, capacity: int):
        # Sentinel nodes — they never hold real data, just mark the boundaries
        self.head = linked_list_utils.ListNode(-1, -1)
        self.tail = linked_list_utils.ListNode(-1, -1)

        self.cache = {}  # key -> ListNode, for O(1) lookup by key
        self.capacity = capacity

        # Link sentinels together to form an empty list: tail <-> head
        self.head.prev = self.tail
        self.tail.next = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        matched_node = self.cache[key]

        # Move to the MRU position (tail end) since it was just accessed
        self._remove_node(matched_node)
        self._insert_node_at_tail(matched_node)

        return matched_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Key exists — remove the old node so we can reinsert at MRU position
            node = self.cache[key]
            self._remove_node(node)
            node.val = value  # update to the new value
        else:
            # Key is new — create a node and register it in the hashmap
            node = linked_list_utils.ListNode(key, value)
            self.cache[key] = node

        # Insert at the MRU end (right after tail sentinel)
        self._insert_node_at_tail(node)

    def _remove_node(self, node: linked_list_utils.ListNode) -> None:
        """Unlink a node from the list by connecting its neighbors to each other."""
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node  # neighbor closer to tail skips over node
        prev_node.next = next_node  # neighbor closer to head skips over node

    def _insert_node_at_tail(self, node: linked_list_utils.ListNode) -> None:
        """Insert node right after the tail sentinel, making it the MRU item."""

        old_last_node = self.tail.next  # the previous MRU node
        self.tail.next = node  # tail now points to the new node
        node.next = old_last_node  # new node points to the old MRU
        old_last_node.prev = node  # old MRU's prev now points to new node
        node.prev = self.tail  # new node links back to tail sentinel

        # If we've exceeded capacity, evict the LRU item (at the head end)
        if len(self.cache) > self.capacity:
            first_node = self.head.prev  # LRU node (closest to head)
            self.head.prev = first_node.prev  # head skips over LRU node
            first_node.prev.next = self.head  # LRU's neighbor now points to head
            del self.cache[first_node.key]  # remove from hashmap too


'''
Note: the following is an implementation that uses `collections.OrderedDict`s, which keep track of
insertion order and allow you to pop off the front and the back, and insert keys onto the back
automatically.

  import collections

  class LRUCache:

      def __init__(self, capacity: int):
          self.cache = collections.OrderedDict()
          self.capacity = capacity

      def get(self, key: int) -> int:
          if key not in self.cache:
              return -1
          
          # move the key to the end to show that it was recently used
          self.cache.move_to_end(key)
          return self.cache[key]

      def put(self, key: int, value: int) -> None:
          if key in self.cache:
              # remove the old value
              self.cache.pop(key)
          elif len(self.cache) >= self.capacity:
              # remove the least recently used item
              self.cache.popitem(last=False)
          # Insert the new key-value pair
          self.cache[key] = value
'''

if __name__ == "__main__":

    assert run_lru_cache(
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
    ) == [None, None, None, 1, None, -1, None, -1, 3, 4]

    assert run_lru_cache(
        ["LRUCache", "put", "put", "put", "put", "get", "get"],
        [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]],
    ) == [None, None, None, None, None, -1, 3]

    assert run_lru_cache(
        [
            "LRUCache",
            "put",
            "put",
            "put",
            "put",
            "get",
            "get",
            "get",
            "get",
            "put",
            "get",
            "get",
            "get",
            "get",
            "get",
        ],
        [[3], [1, 1], [2, 2], [3, 3], [4, 4], [4], [3], [2], [1], [5, 5], [1], [2], [3], [4], [5]],
    ) == [None, None, None, None, None, 4, 3, 2, -1, None, -1, 2, 3, -1, 5]

    print("All test cases passed!")
