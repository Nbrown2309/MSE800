# Developing a smart office system using Python

from factory import DeviceFactory
from config_manager import ConfigManager

# Single Object Instance (Singleton Pattern)
conifg = ConfigManager()
conifg.show_message()

print("=== Smart Office IoT System ===")

user_choice = input(
    "Enter Device (light/fan/ac): "
).lower()

# Factory creates object 
if (device := DeviceFactory.create_device(user_choice)):
    device.device_status()
else:
    print("Invalid device type entered.")