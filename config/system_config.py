import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = ROOT / "config" / "settings.json"


def load_config():
    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def show_config():

    config = load_config()

    print("====== System Config ======")
    print(
        "Project:",
        config["project"]["name"]
    )
    print(
        "Version:",
        config["project"]["version"]
    )
    print("===========================")


if __name__ == "__main__":
    show_config()
