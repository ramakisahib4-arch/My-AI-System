from pathlib import Path


class QwenManager:

    def __init__(self):

        self.model_folder = (
            Path(__file__).parent
        )


    def find_models(self):

        files = []

        for file in self.model_folder.iterdir():

            if file.suffix in [
                ".gguf",
                ".bin",
                ".safetensors"
            ]:

                files.append(
                    file.name
                )

        return files


    def status(self):

        models = self.find_models()

        if models:
            return {
                "status": "ready",
                "models": models
            }

        return {
            "status": "no_model",
            "models": []
        }



if __name__ == "__main__":

    manager = QwenManager()

    print(
        manager.status()
    )
