import json
from pathlib import Path


class DownloadConfigLoader:

    def __init__(self):

        self.file = (
            Path(__file__)
            .resolve()
            .parent.parent
            / "config"
            / "download_config.json"
        )


    def load(self):

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    def get_models(self):

        data = self.load()

        return data.get(
            "models",
            []
        )



if __name__ == "__main__":

    loader = DownloadConfigLoader()

    print(
        loader.get_models()
    )
