from pathlib import Path
import json


class ResourceManager:

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


    def load_resources(self):

        with open(
            self.config,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    def show_resources(self):

        resources = self.load_resources()

        for item, data in resources.items():

            print(
                item,
                "=>",
                data["name"]
            )


if __name__ == "__main__":

    manager = ResourceManager()

    manager.show_resources()
