from pathlib import Path


class BuildManager:

    def check_project(
        self,
        path
    ):

        project = Path(path)

        if not project.exists():

            return {
                "status": "missing"
            }


        files = list(
            project.rglob("*")
        )

        return {
            "status": "ready",
            "files": len(files)
        }


    def prepare_build(
        self,
        path
    ):

        result = self.check_project(
            path
        )

        if result["status"] == "ready":

            return "Build prepared"

        return "Project not ready"



if __name__ == "__main__":

    manager = BuildManager()

    print(
        manager.prepare_build(
            "DemoApp"
        )
    )
