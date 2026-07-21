from scripts.system_check import run_check
from config.system_config import show_config


def start():

    print("==============================")
    print("      My AI System Start")
    print("==============================")

    show_config()

    print()

    run_check()


if __name__ == "__main__":
    start()
