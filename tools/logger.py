from datetime import datetime
from pathlib import Path


class Logger:

    def __init__(self):

        self.file = (
            Path(__file__).parent
            / "system.log"
        )


    def write(self, message):

        time = datetime.now()

        text = (
            f"[{time}] {message}\n"
        )

        with open(
            self.file,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(text)


    def info(self, message):

        self.write(
            "INFO: " + message
        )


    def error(self, message):

        self.write(
            "ERROR: " + message
        )


if __name__ == "__main__":

    log = Logger()

    log.info(
        "AI System Started"
    )
