import json


class AgentResponse:

    def create(
        self,
        result,
        status="success"
    ):

        return {
            "status": status,
            "result": result
        }


    def export_json(
        self,
        data
    ):

        return json.dumps(
            data,
            indent=2,
            ensure_ascii=False
        )



if __name__ == "__main__":

    response = AgentResponse()

    data = response.create(
        "Project created"
    )

    print(
        response.export_json(data)
    )
