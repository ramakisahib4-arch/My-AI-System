import json
from pathlib import Path


class ReleaseManager:

    def __init__(self):

        self.file = (
            Path(__file__).parent
            / "releases.json"
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


    def create_release(
        self,
        version,
        artifact
    ):

        releases = self.load()

        releases.append(
            {
                "version": version,
                "artifact": artifact
            }
        )

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                releases,
                f,
                indent=2,
                ensure_ascii=False
            )

        return "Release created"



if __name__ == "__main__":

    manager = ReleaseManager()

    print(
        manager.create_release(
            "1.0.0",
            "app.apk"
        )
    )

    print(
        manager.load()
    )
