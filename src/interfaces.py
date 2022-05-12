import io


class ConnectorI:
    def connect(self):
        pass

    def fetch(self, remote_location: dict):
        pass

    def store(self, remote_location: dict):
        pass
