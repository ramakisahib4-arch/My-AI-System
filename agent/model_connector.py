from model.qwen_manager import QwenManager


class ModelConnector:

    def __init__(self):

        self.qwen = QwenManager()
        self.current_model = None


    def prepare(self):

        status = self.qwen.status()

        if status["status"] == "ready":

            self.current_model = (
                status["models"][0]
            )

            return (
                "Model ready: "
                + self.current_model
            )

        return "No model found"


    def get_model(self):

        return self.current_model



if __name__ == "__main__":

    connector = ModelConnector()

    print(
        connector.prepare()
    )

    print(
        connector.get_model()
    )
