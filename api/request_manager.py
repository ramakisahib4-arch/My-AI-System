class RequestManager:

    def __init__(self):
        self.requests = []


    def add_request(self, user, message):

        request = {
            "user": user,
            "message": message
        }

        self.requests.append(request)

        return request


    def get_requests(self):

        return self.requests



if __name__ == "__main__":

    manager = RequestManager()

    result = manager.add_request(
        "user",
        "Hello AI"
    )

    print(result)
