import json


class ResponseManager:

    def create_response(
        self,
        message,
        status="success"
    ):

        response = {
            "status": status,
            "message": message
        }

        return response


    def to_json(self, data):

        return json.dumps(
            data,
            ensure_ascii=False,
            indent=2
        )


if __name__ == "__main__":

    manager = ResponseManager()

    result = manager.create_response(
        "AI is ready"
    )

    print(
        manager.to_json(result)
    )
