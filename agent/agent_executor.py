from agent.command_router import CommandRouter


class AgentExecutor:

    def __init__(self):

        self.router = CommandRouter()


    def execute(self, message):

        command = (
            self.router.detect(message)
        )

        return {
            "received": message,
            "action": command
        }



if __name__ == "__main__":

    executor = AgentExecutor()

    print(
        executor.execute(
            "create messenger app"
        )
    )
