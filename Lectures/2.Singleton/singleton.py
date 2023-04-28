from __future__ import annotations
from typing import Mapping
'''
    We use this when we want to ensure that a class has only a single instance.
'''


class ConfigManager:
    _instance: ConfigManager = None

    def __init__(self):
        self.settings: Mapping[str, object] = {}

    @staticmethod
    def get_instance() -> ConfigManager:
        if not ConfigManager._instance:
            ConfigManager._instance = ConfigManager()

        return ConfigManager._instance

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key):
        if key in self.settings:
            return self.settings[key]
