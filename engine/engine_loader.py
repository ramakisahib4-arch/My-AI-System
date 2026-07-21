import json
from pathlib import Path


class EngineLoader:

    def __init__(self):

        self.folder = (
            Path(__file__).parent
        )

        self.config = (
            self.folder
            / "engine_config.json"
        )


    def load_config(self):

        with open(
            self.config,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    def status(self):

        config = self.load_config()

        return {
            "engine": config["engine"],
            "model_type": config["model_type"],
            "ready": config["ready"]
        }



if __name__ == "__main__":

    loader = EngineLoader()

    print(
        loader.status()
    )
