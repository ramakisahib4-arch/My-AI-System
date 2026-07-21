from agent.model_connector import ModelConnector
from engine.engine_connector import EngineConnector


class AIRuntime:

    def __init__(self):

        self.model = ModelConnector()
        self.engine = EngineConnector()


    def initialize(self):

        engine_status = (
            self.engine.connect()
        )

        model_status = (
            self.model.prepare()
        )

        return {
            "engine": engine_status,
            "model": model_status
        }


    def status(self):

        return {
            "engine_connected":
                self.engine.is_connected(),

            "model":
                self.model.get_model()
        }



if __name__ == "__main__":

    runtime = AIRuntime()

    print(
        runtime.initialize()
    )

    print(
        runtime.status()
    )
