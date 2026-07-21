import json
from pathlib import Path


class StateManager:

    def __init__(self):

        self.file = (
            Path(__file__).parent
            / "state.json"
        )


    def load(self):

        if not self.file.exists():

            return {
                "model": "not_ready",
                "engine": "not_ready",
                "agent": "ready"
            }

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    def save(self, state):

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                state,
                f,
                indent=2
            )


if __name__ == "__main__":

    manager = StateManager()

    print(
        manager.load()
    )
