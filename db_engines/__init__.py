class BaseEngine:

    def post(self, uuid, data) -> str:
        raise NotImplemented

    def get(self, uuid) -> str:
        raise NotImplemented

    def process(self, command: str):
        if "ALL" in command:
            print(self)
            return

        method, uuid, *data = command.split(" ")
        data = " ".join(data)
        if method == "POST":
            uuid, data = self.post(uuid, data)
        elif method == "GET":
            uuid, data = self.get(uuid)
        else:
            print("ERROR")
            return
        print("SUCCESS id={} '{}'".format(uuid, data))

    def listen(self):
        while True:
            command = input("[POST | GET | ALL] <id> [ data ]")
            self.process(command)
