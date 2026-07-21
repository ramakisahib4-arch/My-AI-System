class TemplateManager:

    def __init__(self):

        self.templates = {
            "android": [
                "app",
                "gradle",
                "src"
            ],

            "web": [
                "frontend",
                "backend"
            ],

            "python": [
                "src",
                "tests"
            ]
        }


    def get_template(
        self,
        project_type
    ):

        return self.templates.get(
            project_type,
            []
        )


    def list_templates(self):

        return list(
            self.templates.keys()
        )



if __name__ == "__main__":

    manager = TemplateManager()

    print(
        manager.list_templates()
    )

    print(
        manager.get_template(
            "android"
        )
    )
