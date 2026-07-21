from tools.tools_manager import ToolsManager


class ToolConnector:

    def __init__(self):

        self.manager = ToolsManager()


    def setup_default_tools(self):

        tools = [
            "file_manager",
            "project_builder",
            "command_runner"
        ]

        for tool in tools:

            self.manager.register_tool(
                tool
            )


    def get_tools(self):

        return self.manager.list_tools()



if __name__ == "__main__":

    connector = ToolConnector()

    connector.setup_default_tools()

    print(
        connector.get_tools()
    )
