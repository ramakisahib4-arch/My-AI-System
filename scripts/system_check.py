from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def check_folder(name):
    path = ROOT / name

    if path.exists():
        return "OK"
    else:
        return "Missing"


def run_check():

    components = [
        "model",
        "engine",
        "agent",
        "tools",
        "api"
    ]

    print("====== System Check ======")

    for item in components:
        print(
            f"{item}: {check_folder(item)}"
        )

    print("==========================")


if __name__ == "__main__":
    run_check()
