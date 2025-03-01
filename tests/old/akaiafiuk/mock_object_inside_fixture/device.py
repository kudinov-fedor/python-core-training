class Device:
    def __init__(self):
        self.version = "1.1"

    def get_version(self):
        return self.version

    def validate_device(self):
        verdict = True
        if self.get_version() is None:
            verdict = False
        if not verdict:
            raise RuntimeError("Self check is failed. Device is not ready for use.")
