NAME = "street animal"


def say(self):
    print("Hi I am {}".format(self.NAME))


def move(self, new_position):
    self.POSITION = new_position


def get_position(self):
    return self.POSITION


def feed():
    raise NotImplemented


def get_name(self):
    if hasattr(self, "NAME"):
        return self.NAME
    return self.BASE.NAME


# create new ITEM
def new(base):
    from copy import copy

    from empty import empty
    item = copy(empty)  # todo you can not copy module, does not work

    item.BASE = base
    return item


# pre setup item
def init(self, position, name=None):
    self.POSITION = position
    if name:
        self.NAME = name


# create and pre setup item
def create(base, *args, **kwargs):
    item = new(base)
    item.BASE.init(item, *args, **kwargs)
    return item
