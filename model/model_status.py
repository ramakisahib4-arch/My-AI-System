from pathlib import Path
import json


class ModelStatus:

    def __init__(self):

        self.file = (
            Path(__file__).parent
            / "model_status.json"
        )


    def load(self):

        if not self.file.exists():

            return {
                "model": "qwen3_4b",
                "downloaded": False,
                "ready": False
            }

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    def update(
        self,
        downloaded,
        ready
    ):

        data = {
            "model": "qwen3_4b",
            "downloaded": downloaded,
            "ready": ready
        }

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=2
            )

        return data



if __name__ == "__main__":

    status = ModelStatus()

    print(
        status.load()
    )
