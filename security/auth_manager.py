import hashlib


class AuthManager:

    def __init__(self):

        self.users = {}


    def create_user(
        self,
        email,
        password
    ):

        hashed = hashlib.sha256(
            password.encode()
        ).hexdigest()


        self.users[email] = {
            "password": hashed
        }


        return {
            "status": "created",
            "email": email
        }


    def login(
        self,
        email,
        password
    ):

        hashed = hashlib.sha256(
            password.encode()
        ).hexdigest()


        user = self.users.get(
            email
        )


        if user and user["password"] == hashed:

            return True

        return False



if __name__ == "__main__":

    auth = AuthManager()

    print(
        auth.create_user(
            "test@mail.com",
            "123456"
        )
    )

    print(
        auth.login(
            "test@mail.com",
            "123456"
        )
    )
