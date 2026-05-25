from devices import SmartLight, SmartFan, SmartAirConditioner


class DeviceFactory:

    @staticmethod
    def create_device(device_type):

        if device_type == "light":
            return SmartLight()

        elif device_type == "fan":
            return SmartFan()

        elif device_type == "ac":
            return SmartAirConditioner()

        else:
            return None