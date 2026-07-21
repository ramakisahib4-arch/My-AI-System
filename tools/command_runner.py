import subprocess


class CommandRunner:

    def run(self, command):

        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )

            return {
                "output": result.stdout,
                "error": result.stderr,
                "code": result.returncode
            }

        except Exception as e:

            return {
                "error": str(e)
            }


if __name__ == "__main__":

    runner = CommandRunner()

    print(
        runner.run(
            "python --version"
        )
    )
