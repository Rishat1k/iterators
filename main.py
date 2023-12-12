class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.count = 0
        self.nested_count = 0
        return self

    def __next__(self):
        if self.count < len(self.list_of_list):
            self.lst = self.list_of_list[self.count]
            if self.nested_count < len(self.lst) - 1:
                self.nested_count += 1
                return self.lst[self.nested_count - 1]
            else:
                self.count += 1
                self.nested_count = 0
                return self.lst[-1]
        else:
            raise StopIteration



def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()