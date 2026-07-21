import json
from pathlib import Path


class UserProfile:

    def __init__(self):

        self.file = (
            Path(__file__).parent
            / "user_profile.json"
        )


    def create(
        self,
        name,
        email
    ):

        profile = {
            "name": name,
            "email": email
        }

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                profile,
                f,
                indent=2,
                ensure_ascii=False
            )

        return profile


    def get(self):

        if not self.file.exists():

            return {}

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)



if __name__ == "__main__":

    user = UserProfile()

    print(
        user.create(
            "User",
            "user@email.com"
        )
    )

    print(
        user.get()
    )
