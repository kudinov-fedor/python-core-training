import bisect

from db_engines import BaseEngine


class SMTableEngine(BaseEngine):

    def __init__(self):
        self.data = []

    def post(self, uuid, data) -> tuple:
        index = bisect.bisect_left(self.data, (uuid, ""))

        if len(self.data) <= index:
            self.data.append((uuid, data))
        elif self.data[index][0] == uuid:
            self.data[index] = (uuid, data)
        else:
            self.data.insert(index, (uuid, data))

        # todo if to big: Dump to file

        return uuid, data

    def get(self, uuid) -> tuple:
        index = bisect.bisect_right(self.data, (uuid, ""))
        uuid, data = self.data[index]

        # todo if not in data FInd in files

        return uuid, data

    def __str__(self):
        return str(self.data)


if __name__ == "__main__":
    SMTableEngine().listen()
