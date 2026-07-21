from agent.agent_executor import AgentExecutor
from agent.agent_response import AgentResponse


class AIPipeline:

    def __init__(self):

        self.executor = AgentExecutor()
        self.response = AgentResponse()


    def run(self, message):

        result = self.executor.execute(
            message
        )

        return self.response.create(
            result
        )


if __name__ == "__main__":

    pipeline = AIPipeline()

    output = pipeline.run(
        "create android app"
    )

    print(output)
