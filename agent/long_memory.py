import json
from pathlib import Path


class LongMemory:

    def __init__(self):

        self.file = (
            Path(__file__).parent
            / "long_memory.json"
        )


    def read(self):

        if not self.file.exists():

            return {}

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    def remember(
        self,
        key,
        value
    ):

        data = self.read()

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


        return "Memory saved"



if __name__ == "__main__":

    memory = LongMemory()

    print(
        memory.remember(
            "project",
            "My AI System"
        )
    )

    print(
        memory.read()
    )
