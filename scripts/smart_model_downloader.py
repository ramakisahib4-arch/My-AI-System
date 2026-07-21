from scripts.download_config_loader import DownloadConfigLoader
from scripts.model_downloader import ModelDownloader


class SmartModelDownloader:

    def __init__(self):

        self.config = DownloadConfigLoader()
        self.downloader = ModelDownloader()


    def list_available_models(self):

        return self.config.get_models()


    def prepare_downloads(self):

        models = self.list_available_models()

        result = []

        for model in models:

            if model.get("enabled"):

                result.append(
                    {
                        "id": model["id"],
                        "file": model["file_name"],
                        "url": model["download_url"]
                    }
                )

        return result



if __name__ == "__main__":

    manager = SmartModelDownloader()

    print(
        manager.prepare_downloads()
    )
