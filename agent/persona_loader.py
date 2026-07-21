import json
from pathlib import Path


class PersonaLoader:

    def __init__(self):

        self.file = (
            Path(__file__)
            .resolve()
            .parent.parent
            / "config"
            / "persona.json"
        )


    def load(self):

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    def get_name(self):

        persona = self.load()

        return persona["name"]



if __name__ == "__main__":

    loader = PersonaLoader()

    print(
        loader.get_name()
    )
