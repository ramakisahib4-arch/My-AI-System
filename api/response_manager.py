import json
from datetime import datetime


class ResponseManager:

    def success(
        self,
        data
    ):

        return {
            "status": "success",
            "time": str(
                datetime.now()
            ),
            "data": data
        }


    def error(
        self,
        message
    ):

        return {
            "status": "error",
            "message": message,
            "time": str(
                datetime.now()
            )
        }


    def to_json(
        self,
        response
    ):

        return json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )



if __name__ == "__main__":

    manager = ResponseManager()

    result = manager.success(
        "AI Ready"
    )

    print(
        manager.to_json(
            result
        )
    )
