import json
from pathlib import Path


class ModelManager:

    def __init__(self):

        self.root = (
            Path(__file__)
            .resolve()
            .parent.parent
        )

        self.config = (
            self.root
            / "config"
            / "models.json"
        )


    def load_models(self):

        with open(
            self.config,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    def list_models(self):

        models = self.load_models()

        result = []

        for name, data in models.items():

            result.append(
                {
                    "type": name,
                    "name": data["name"]
                }
            )

        return result



if __name__ == "__main__":

    manager = ModelManager()

    print(
        manager.list_models()
    )
