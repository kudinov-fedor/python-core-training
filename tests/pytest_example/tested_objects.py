GLOBAL_ITEM = 123


class X:

    def __init__(self):
        self.x = 123

    def y(self):
        raise AssertionError

    def return_global_item(self):
        return GLOBAL_ITEM
