from agent.ai_core import AICore
from tools.tools_manager import ToolsManager


class AgentController:

    def __init__(self):

        self.ai = AICore()
        self.tools = ToolsManager()


    def initialize(self):

        self.ai.load_model(
            "Qwen3"
        )

        self.tools.register_tool(
            "file_manager"
        )

        self.tools.register_tool(
            "project_builder"
        )


    def handle(self, request):

        return self.ai.ask(
            request
        )


if __name__ == "__main__":

    agent = AgentController()

    agent.initialize()

    print(
        agent.handle(
            "Create Android app"
        )
    )
