class LanguageManager:

    def __init__(self):

        self.languages = [
            "fa",
            "ps",
            "en"
        ]

        self.current = "fa"


    def set_language(
        self,
        language
    ):

        if language in self.languages:

            self.current = language

            return True

        return False


    def get_language(self):

        return self.current



if __name__ == "__main__":

    manager = LanguageManager()

    print(
        manager.get_language()
    )

    manager.set_language(
        "en"
    )

    print(
        manager.get_language()
    )
