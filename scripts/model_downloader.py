from pathlib import Path
import urllib.request


class ModelDownloader:

    def __init__(self):

        self.folder = (
            Path(__file__)
            .resolve()
            .parent.parent
            / "model"
        )

        self.folder.mkdir(
            exist_ok=True
        )


    def download(
        self,
        url,
        filename
    ):

        path = (
            self.folder
            / filename
        )

        print(
            "Downloading:",
            filename
        )

        urllib.request.urlretrieve(
            url,
            path
        )

        return str(path)



if __name__ == "__main__":

    downloader = ModelDownloader()

    print(
        "Downloader ready"
    )
