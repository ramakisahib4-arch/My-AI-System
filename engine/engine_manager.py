from pathlib import Path


class EngineManager:

    def __init__(self):

        self.engine_path = (
            Path(__file__)
            .resolve()
            .parent
        )

        self.status = "not_loaded"


    def check_engine(self):

        files = list(
            self.engine_path.iterdir()
        )

        if len(files) > 1:
            self.status = "available"
        else:
            self.status = "empty"

        return self.status


    def load_engine(self):

        if self.status == "available":
            return "Engine loaded"

        return "Engine not ready"



if __name__ == "__main__":

    engine = EngineManager()

    print(
        engine.check_engine()
    )

    print(
        engine.load_engine()
    )
