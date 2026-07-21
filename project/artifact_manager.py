from pathlib import Path
import shutil


class ArtifactManager:

    def __init__(self):

        self.folder = Path(
            "artifacts"
        )

        self.folder.mkdir(
            exist_ok=True
        )


    def save(
        self,
        source
    ):

        file = Path(source)

        if not file.exists():

            return "File not found"


        target = (
            self.folder
            / file.name
        )

        shutil.copy(
            file,
            target
        )

        return str(target)


    def list_artifacts(self):

        return [
            f.name
            for f in self.folder.iterdir()
        ]



if __name__ == "__main__":

    manager = ArtifactManager()

    print(
        manager.list_artifacts()
    )
