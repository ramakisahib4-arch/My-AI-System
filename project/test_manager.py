from pathlib import Path


class TestManager:

    def scan_tests(
        self,
        path
    ):

        folder = Path(path)

        if not folder.exists():

            return []


        tests = []

        for file in folder.rglob("*"):

            if "test" in file.name.lower():

                tests.append(
                    str(file)
                )

        return tests


    def run_check(
        self,
        path
    ):

        tests = self.scan_tests(
            path
        )

        return {
            "tests_found": len(tests),
            "files": tests
        }



if __name__ == "__main__":

    manager = TestManager()

    print(
        manager.run_check(
            "DemoApp"
        )
    )
