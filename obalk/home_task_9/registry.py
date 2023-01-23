from typing import List


class Registry:
    instances: List["Registry"] = []

    def __new__(cls, *args, **kwargs):
        element = super().__new__(cls)
        cls.instances.append(element)
        return element

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self):
        return f"{id(self)=}, {self.name=}"


if __name__ == "__main__":
    first = Registry("first object")
    second = Registry("second object")

    print(Registry.instances)
    assert len(Registry.instances) == 2
    assert Registry.instances[0].name == "first object"
    assert Registry.instances[1].name == "second object"
