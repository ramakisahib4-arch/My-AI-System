from agent.ai_core import AICore


class AIService:

    def __init__(self):

        self.ai = AICore()


    def load(self, model):

        self.ai.load_model(model)


    def process(self, prompt):

        return self.ai.ask(prompt)



if __name__ == "__main__":

    service = AIService()

    service.load(
        "Qwen3"
    )

    print(
        service.process(
            "Build an app"
        )
    )
