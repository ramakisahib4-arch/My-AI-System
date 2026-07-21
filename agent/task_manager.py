class TaskManager:

    def __init__(self):

        self.tasks = []


    def create_task(
        self,
        title
    ):

        task = {
            "title": title,
            "status": "pending"
        }

        self.tasks.append(task)

        return task


    def complete_task(
        self,
        index
    ):

        if index < len(self.tasks):

            self.tasks[index]["status"] = "done"


    def list_tasks(self):

        return self.tasks



if __name__ == "__main__":

    manager = TaskManager()

    manager.create_task(
        "Create Android App"
    )

    manager.create_task(
        "Test Project"
    )

    manager.complete_task(0)

    print(
        manager.list_tasks()
    )
