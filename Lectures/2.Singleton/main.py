from singleton import ConfigManager


def main():
    manager = ConfigManager.get_instance()
    manager.set("name", "Mosh")

    other = ConfigManager.get_instance()
    print(other.get("name"))


if __name__ == '__main__':
    main()
