class Override:
    created_instances = []

    def __init__(self):
        Override.created_instances.append(self)


obj1 = Override()
obj2 = Override()
print(Override.created_instances)
