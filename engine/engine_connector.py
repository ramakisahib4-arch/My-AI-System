from engine.engine_loader import EngineLoader


class EngineConnector:

    def __init__(self):

        self.loader = EngineLoader()
        self.connected = False


    def connect(self):

        status = self.loader.status()

        if status["engine"]:

            self.connected = True

            return {
                "status": "connected",
                "engine": status["engine"]
            }

        return {
            "status": "failed"
        }


    def is_connected(self):

        return self.connected



if __name__ == "__main__":

    engine = EngineConnector()

    print(
        engine.connect()
    )

    print(
        engine.is_connected()
    )
