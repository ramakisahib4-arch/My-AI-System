import json
from pathlib import Path


class DownloadManager:

    def __init__(self):
        self.root = Path(__file__).resolve().parent.parent
        self.config = self.root / "config"

    def load_models(self):
        with open(self.config / "models.json", "r", encoding="utf-8") as f:
            return json.load(f)

    def check_structure(self):
        models = self.load_models()

        print("====== AI System Components ======")

        for component, info in models.items():
            folder = self.root / info["path"]

            status = "OK" if folder.exists() else "Missing"

            print(
                f"{component}: {info['name']} | "
                f"Folder: {info['path']} | "
                f"Status: {status}"
            )

        print("==================================")


if __name__ == "__main__":
    manager = DownloadManager()
    manager.check_structure()
