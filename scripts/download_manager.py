import json
from pathlib import Path


class DownloadManager:

    def __init__(self):
        self.root = Path(__file__).resolve().parent.parent
        self.config = self.root / "config"

    def load_models(self):
        with open(self.config / "models.json", "r", encoding="utf-8") as f:
            return json.load(f)

    def show_components(self):
        data = self.load_models()

        print("========== AI Components ==========")

        for key, value in data.items():
            print(f"{key} : {value['name']}")

        print("===================================")


if __name__ == "__main__":
    DownloadManager().show_components()
