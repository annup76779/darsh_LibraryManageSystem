import json
import os


class Configuration:
    """
    Configuration class to handle loading and accessing configuration settings.
    """
    def __init__(self):
        self.__config = None  # readonly variable

    @property
    def config(self):
        """
        Property to get the configuration data. Loads the configuration if not already loaded.
        """
        if self.__config is None:
            self.load_config()
        return self.__config

    def load_config(self):
        """
        Loads the configuration from the appsettings.json file.
        """
        config_path = os.path.join(os.path.dirname(__file__), "appsettings.json")
        try:
            with open(config_path, 'r') as config_file:
                self.__config = json.load(config_file)
        except FileNotFoundError:
            print(f"Configuration file not found: {config_path}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the configuration file: {config_path}")


__config__ = Configuration().config
