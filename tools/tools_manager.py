class ToolsManager:

    def __init__(self):
        self.tools = []


    def register_tool(self, name):

        self.tools.append(name)

        print(
            "Tool added:",
            name
        )


    def list_tools(self):

        return self.tools



if __name__ == "__main__":

    manager = ToolsManager()

    manager.register_tool(
        "file_builder"
    )

    manager.register_tool(
        "web_search"
    )

    print(
        manager.list_tools()
    )
