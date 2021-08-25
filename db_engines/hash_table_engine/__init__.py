from db_engines import BaseEngine


class HashTableEngine(BaseEngine):
    def __init__(self):
        self.data = {}

    def post(self, uuid, data) -> tuple:
        self.data[uuid] = data
        return uuid, data

    def get(self, uuid) -> tuple:
        data = self.data[uuid]
        return uuid, data

    def __str__(self):
        return str(self.data)


if __name__ == "__main__":
    HashTableEngine().listen()
