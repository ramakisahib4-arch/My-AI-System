class PermissionManager:

    def __init__(self):

        self.permissions = {
            "file_manager": True,
            "project_builder": True,
            "command_runner": False
        }


    def check(self, tool):

        return self.permissions.get(
            tool,
            False
        )


    def set_permission(
        self,
        tool,
        value
    ):

        self.permissions[tool] = value



if __name__ == "__main__":

    manager = PermissionManager()

    print(
        manager.check(
            "file_manager"
        )
    )

    print(
        manager.check(
            "command_runner"
        )
    )
