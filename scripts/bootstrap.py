
import json
from pathlib import Path


class Bootstrap:

    def __init__(self):
        self.root = Path(__file__).resolve().parent.parent
        self.config = self.root / "config"

    def load_settings(self):
        with open(self.config / "settings.json", "r", encoding="utf-8") as f:
            return json.load(f)

    def start(self):
        settings = self.load_settings()

        print("===================================")
        print("      My AI System Bootstrap")
        print("===================================")
        print(f"Project : {settings['project']['name']}")
        print(f"Version : {settings['project']['version']}")
        print("Bootstrap Ready")


if __name__ == "__main__":
    Bootstrap().start()
