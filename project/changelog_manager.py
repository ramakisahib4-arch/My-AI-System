import json
from pathlib import Path


class ChangelogManager:

    def __init__(self):

        self.file = (
            Path(__file__).parent
            / "changelog.json"
        )


    def load(self):

        if not self.file.exists():

            return []

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    def add_change(
        self,
        version,
        change
    ):

        logs = self.load()

        logs.append(
            {
                "version": version,
                "change": change
            }
        )

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                logs,
                f,
                indent=2,
                ensure_ascii=False
            )

        return "Change added"



if __name__ == "__main__":

    manager = ChangelogManager()

    print(
        manager.add_change(
            "1.0.0",
            "Initial AI system"
        )
    )

    print(
        manager.load()
    )
