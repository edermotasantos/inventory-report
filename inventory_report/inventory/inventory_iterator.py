from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, items_in_stock):
        self._items_in_stock = items_in_stock
        self._index = 0

    def __next__(self):
        try:
            current_value = self._items_in_stock[self._index]
        except IndexError:
            raise StopIteration()
        else:
            self._index += 1
            return current_value
