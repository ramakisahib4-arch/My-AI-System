import os
import json
from pathlib import Path


class SecretsManager:

    def __init__(self):

        self.file = (
            Path(__file__).parent
            / "secrets.json"
        )


    def load(self):

        if not self.file.exists():

            return {}

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    def get(
        self,
        key
    ):

        secrets = self.load()

        return secrets.get(
            key
        )


    def set(
        self,
        key,
        value
    ):

        secrets = self.load()

        secrets[key] = value

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                secrets,
                f,
                indent=2
            )

        return True



if __name__ == "__main__":

    manager = SecretsManager()

    manager.set(
        "example",
        "value"
    )

    print(
        manager.get(
            "example"
        )
    )
