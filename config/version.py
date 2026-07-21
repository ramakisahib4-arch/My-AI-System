class VersionManager:

    def __init__(self):

        self.version = "1.0.0"


    def get_version(self):

        return self.version


    def update_version(
        self,
        new_version
    ):

        self.version = new_version

        return self.version



if __name__ == "__main__":

    manager = VersionManager()

    print(
        manager.get_version()
    )

    print(
        manager.update_version(
            "1.1.0"
        )
    )
