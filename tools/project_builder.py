from pathlib import Path


class ProjectBuilder:

    def create_project(
        self,
        name
    ):

        project = Path(name)

        project.mkdir(
            exist_ok=True
        )

        (project / "src").mkdir(
            exist_ok=True
        )

        (project / "README.md").write_text(
            "# " + name
        )

        return (
            f"Project {name} created"
        )


if __name__ == "__main__":

    builder = ProjectBuilder()

    print(
        builder.create_project(
            "TestProject"
        )
    )
