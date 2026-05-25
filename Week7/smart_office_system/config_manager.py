# Creating a configuration manager for the smart office system

class ConfigManager:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance.config = {}
        return cls._instance
    
    def show_message(self):
        print("This is the configuration manager for the smart office system.")
        