class CommandRouter:

    def __init__(self):

        self.commands = {
            "create": "project_builder",
            "file": "file_manager",
            "run": "command_runner"
        }


    def detect(self, message):

        text = message.lower()

        for key, tool in self.commands.items():

            if key in text:

                return {
                    "tool": tool,
                    "command": key
                }

        return {
            "tool": "ai_core",
            "command": "chat"
        }



if __name__ == "__main__":

    router = CommandRouter()

    print(
        router.detect(
            "create android app"
        )
    )
