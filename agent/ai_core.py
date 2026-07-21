class AICore:

    def __init__(self):
        self.model = None
        self.status = "initialized"


    def load_model(self, model_path):

        self.model = model_path
        self.status = "model_loaded"

        print(
            "Model loaded:",
            model_path
        )


    def ask(self, prompt):

        if self.model is None:
            return "Model is not loaded"

        return (
            "AI received: "
            + prompt
        )


if __name__ == "__main__":

    ai = AICore()

    ai.load_model(
        "Qwen3"
    )

    print(
        ai.ask(
            "Hello AI"
        )
    )
