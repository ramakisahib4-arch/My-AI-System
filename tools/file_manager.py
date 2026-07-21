from pathlib import Path


class FileManager:

    def create_file(
        self,
        path,
        content=""
    ):

        file = Path(path)

        file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        file.write_text(
            content,
            encoding="utf-8"
        )

        return f"Created: {path}"


    def read_file(
        self,
        path
    ):

        file = Path(path)

        if not file.exists():
            return "File not found"

        return file.read_text(
            encoding="utf-8"
        )


if __name__ == "__main__":

    manager = FileManager()

    print(
        manager.create_file(
            "test/example.txt",
            "Hello AI"
        )
    )
