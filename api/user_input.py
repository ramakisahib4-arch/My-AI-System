class UserInput:

    def __init__(self):
        self.history = []


    def receive(self, message):

        data = {
            "message": message
        }

        self.history.append(data)

        return data


    def get_history(self):

        return self.history



if __name__ == "__main__":

    user = UserInput()

    print(
        user.receive(
            "Build an app"
        )
    )
