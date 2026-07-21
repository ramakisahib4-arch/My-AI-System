from datetime import datetime


class HealthCheck:

    def status(self):

        return {
            "status": "online",
            "service": "AI System",
            "time": str(
                datetime.now()
            )
        }



if __name__ == "__main__":

    check = HealthCheck()

    print(
        check.status()
    )
