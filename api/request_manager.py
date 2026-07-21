import json


class RequestManager:

    def parse(
        self,
        data
    ):

        if isinstance(
            data,
            str
        ):

            try:

                return json.loads(
                    data
                )

            except:

                return {
                    "message": data
                }


        return data


    def validate(
        self,
        request
    ):

        if "message" in request:

            return True

        return False



if __name__ == "__main__":

    manager = RequestManager()

    request = manager.parse(
        '{"message":"Hello AI"}'
    )

    print(request)

    print(
        manager.validate(
            request
        )
    )
