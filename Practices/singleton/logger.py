from __future__ import annotations


class Logger:
    _instance: Logger = None

    def __init__(self, filename):
        self.filename = filename

    def write(self, message: str):
        print("Writing a message to the log.")

    @staticmethod
    def get_instance(filename) -> Logger:
        if not Logger._instance:
            print(f"Creating new logger on file {filename}")
            Logger._instance = Logger(filename)

        return Logger._instance


def main():
    logger = Logger.get_instance("File1.py")
    logger1 = Logger.get_instance("File1.py")


if __name__ == '__main__':
    main()
