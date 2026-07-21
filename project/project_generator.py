from pathlib import Path

from project.template_manager import TemplateManager


class ProjectGenerator:

    def __init__(self):

        self.templates = TemplateManager()


    def create(
        self,
        name,
        project_type
    ):

        folders = (
            self.templates
            .get_template(project_type)
        )

        root = Path(name)

        root.mkdir(
            exist_ok=True
        )

        for folder in folders:

            (
                root / folder
            ).mkdir(
                exist_ok=True
            )

        return {
            "project": name,
            "type": project_type,
            "folders": folders
        }



if __name__ == "__main__":

    generator = ProjectGenerator()

    print(
        generator.create(
            "DemoApp",
            "python"
        )
    )
