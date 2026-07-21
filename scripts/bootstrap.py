from config.state_manager import StateManager
from agent.ai_runtime import AIRuntime


class Bootstrap:

    def __init__(self):

        self.state = StateManager()
        self.runtime = AIRuntime()


    def start(self):

        print(
            "Starting AI System..."
        )

        result = (
            self.runtime.initialize()
        )

        self.state.save(
            {
                "system": "running",
                "runtime": result
            }
        )

        return result



if __name__ == "__main__":

    boot = Bootstrap()

    print(
        boot.start()
    )
