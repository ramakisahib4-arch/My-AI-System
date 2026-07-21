import json
from pathlib import Path


class ConversationManager:

    def __init__(self):

        self.file = (
            Path(__file__).parent
            / "conversations.json"
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


    def add_message(
        self,
        role,
        message
    ):

        data = self.load()

        data.append(
            {
                "role": role,
                "message": message
            }
        )

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=2,
                ensure_ascii=False
            )


    def get_history(self):

        return self.load()



if __name__ == "__main__":

    chat = ConversationManager()

    chat.add_message(
        "user",
        "Hello AI"
    )

    print(
        chat.get_history()
    )
