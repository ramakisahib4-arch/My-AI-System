import json
from pathlib import Path


class Memory:

    def __init__(self):

        self.file = (
            Path(__file__).parent
            / "memory.json"
        )


    def save(self, key, value):

        data = self.load()

        data[key] = value

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                data,
                f,
                indent=2,
                ensure_ascii=False
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


if __name__ == "__main__":

    memory = Memory()

    memory.save(
        "status",
        "ready"
    )

    print(
        memory.load()
    )
