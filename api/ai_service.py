from agent.pipeline import AIPipeline


class AIService:

    def __init__(self):

        self.pipeline = AIPipeline()


    def chat(
        self,
        message
    ):

        return self.pipeline.run(
            message
        )


if __name__ == "__main__":

    service = AIService()

    print(
        service.chat(
            "Hello AI"
        )
    )
