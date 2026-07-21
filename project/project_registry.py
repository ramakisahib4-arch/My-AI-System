import json
from pathlib import Path


class ProjectRegistry:

    def __init__(self):

        self.file = (
            Path(__file__).parent
            / "projects.json"
        )


    def load(self):

        if not self.file.exists():

            return []

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    def add_project(
        self,
        name,
        path
    ):

        projects = self.load()

        projects.append(
            {
                "name": name,
                "path": path
            }
        )

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                projects,
                f,
                indent=2,
                ensure_ascii=False
            )

        return "Project registered"



if __name__ == "__main__":

    registry = ProjectRegistry()

    print(
        registry.add_project(
            "TestApp",
            "/projects/test"
        )
    )

    print(
        registry.load()
    )
