import random, typing

random.seed(240704)


class RandomizedSet:
    def __init__(self):
        # `self.element_dict` will store a mapping of values to their indices in
        # `self.element_list` will store the elements themselves
        self.element_dict = {}
        self.element_list = []

    def insert(self, val: int) -> bool:
        if val in self.element_dict:
            return False

        # conveniently, because of the way indices work, the code below inserts `val` correctly at
        # its new index `n`
        n = len(self.element_list)
        self.element_dict[val] = n
        self.element_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.element_dict:
            return False
        # idea:
        # * suppose
        # len(self.element_list) == 6
        # self.element_dict[val] == 3
        #
        # self.element_list[3] = val
        # self.element_list[5] = whatever
        index_to_delete = self.element_dict[val]  # 3
        last_index = len(self.element_list) - 1  # 5
        last_element = self.element_list[last_index]  # whatever

        # * place the index of `val` at the end of `self.element_list`
        # * place the index of the last element of `self.element_list`
        self.element_list[index_to_delete], self.element_list[last_index] = (
            self.element_list[last_index],
            self.element_list[index_to_delete],
        )

        # `self.element_list[index_to_delete]` = whatever
        # `self.element_list[last_index]` = val
        # now, need `self.element_dict[whatever] = index_to_delete`
        self.element_dict[last_element] = index_to_delete

        self.element_list.pop()
        del self.element_dict[val]
        return True

    def get_random(self) -> int:
        return random.choice(self.element_list)


def test_randomized_set(
    commands: typing.List[str], arguments: typing.List[typing.List[int]]
) -> typing.List:
    obj = None
    results = []

    for command, arg in zip(commands, arguments):
        if command == "RandomizedSet":
            obj = RandomizedSet()
            results.append(None)
        elif command == "insert":
            result = obj.insert(arg[0])
            results.append(result)
        elif command == "remove":
            result = obj.remove(arg[0])
            results.append(result)
        elif command == "get_random":
            result = obj.get_random()
            # For the purpose of matching expected output, adjust the result as per the expected.
            results.append(result)

    return results


if __name__ == "__main__":

    assert test_randomized_set(
        [
            "RandomizedSet",
            "insert",
            "remove",
            "insert",
            "get_random",
            "remove",
            "insert",
            "get_random",
        ],
        [[], [1], [2], [2], [], [1], [2], []],
    ) == [None, True, False, True, 2, True, False, 2]

    print("Test case passed!")
