"""
The SmartDevices class represents a smart device that has a toggle switch that can be turned on and off.
The class has the following methods:

init : initializes the class by setting the 'switched_on' attribute to False.
toggle_switch : toggles the switch status.
get_switch_status : returns the current switch status.
set_switch_status : sets the switch status of all devices.

"""


class SmartDevices:
    def __init__(self):
        self.switched_on = False

    def toggle_switch(self):
        self.switched_on = not self.switched_on

    def get_switch_status(self):
        return self.switched_on

    def set_switch_status(self, all_the_devices):
        self.switched_on = all_the_devices


"""
The SmartPlug class is a subclass of SmartDevices, which represents a smart plug with additional methods to set and get the consumption rate.
It has the following methods:

init : initializes the class by calling the parent class's init method and setting the 'consumption_rate' attribute to 0.
get_consumption_rate : returns the current consumption rate.
set_consumption_rate : sets the consumption rate to a new value (between 0 and 150).
str : returns a string representation of the SmartPlug object.
"""


class SmartPlug(SmartDevices):
    def __init__(self):
        super().__init__()
        self.consumption_rate = 0

    def get_consumption_rate(self):
        return self.consumption_rate

    def set_consumption_rate(self, new_rate):
        if 0 <= new_rate <= 150:
            self.consumption_rate = new_rate
        else:
            print("value exceeds the range")

    def __str__(self):
        if self.switched_on:
            output = "plug: {} / ON".format(self.switched_on)
        else:
            output = "plug: {} / OFF".format(self.switched_on)

            # output = output + "Status: {}\n".format(self.switched_on)
        output = output + " Consumption Rate: {:.2f}".format(self.consumption_rate)
        return output


def test_smart_plug():
    plug = SmartPlug()  # Create an instance of the SmartPlug class.
    plug.toggle_switch()  # 1 Toggle this plug by calling the toggleSwitch method.
    plug.toggle_switch()  # 2
    plug.toggle_switch()  # 3
    plug.toggle_switch()  # 4
    print(plug.get_switch_status())  # Print the value of switchedOn using the appropriate accessor method.
    print(plug.get_consumption_rate())  # Print the value of consumptionRate
    plug.set_consumption_rate(11)  # set it to a new value
    print(plug.get_consumption_rate())  # and then print it again.

    print(plug)  # Print the SmartPlug object


# test_smart_plug()

# wash mode options

options = {
    "Daily wash": "Daily wash",
    "Quick wash": "Quick wash",
    "Eco": "Eco"
}

# options = ["Daily wash", "Quick wash", "Eco"]

"""
The SmartWashingMachine class is a subclass of SmartDevices, which represents a smart washing machine with additional methods to set and get the wash mode options.
It has the following methods:

init : initializes the class by calling the parent class's init method and setting the 'wash_mode' attribute to 'Daily wash'.
get_washing_machine_status : returns the current switch status of the washing machine.
get_wash_mode_options : returns the current wash mode.
set_wash_mode_options : sets the wash mode to a new value (from a predefined dictionary of wash modes).
str : returns a string representation of the SmartWashingMachine object.
"""


class SmartWashingMachine(SmartDevices):
    def __init__(self):
        super().__init__()
        self.wash_mode = "Daily wash"

    def get_washing_machine_status(self):
        return self.switched_on

    def get_wash_mode_options(self):
        return self.wash_mode

    def set_wash_mode_options(self, option):
        if option in options:
            self.wash_mode = options[option]
        else:
            print("Option not available!")

    def __str__(self):
        if self.switched_on:
            output = "WashMac: {} / ON".format(self.switched_on)
        else:
            output = "WashMac: {} / OFF".format(self.switched_on)

        # output = output + "Status: {}\n".format(self.switched_on)
        output = output + " Mode:{}".format(self.wash_mode)
        return output


def test_washing_machine():
    washing_machine = SmartWashingMachine()
    washing_machine.toggle_switch()
    print(washing_machine.get_washing_machine_status())
    print(washing_machine.get_wash_mode_options())
    washing_machine.set_wash_mode_options("Quick wash")
    print(washing_machine.get_wash_mode_options())
    print(washing_machine)


test_washing_machine()
# this dictionary is used as
device_dic = {
    "Smart plug": SmartPlug(),
    "Custom": SmartWashingMachine()
}
"""
The SmartHome class represents a smart home that contains a list of smart devices.
It has the following methods:

init : initializes the class by creating an empty list of devices.
get_devices : returns the list of devices.
get_device_at : returns the device at a specified index.
add_device : adds a device to the list.
toggle_switch : toggles the switch of the device at a specified index.
turn_on_all : turns on all the devices in the list.
turn_all_off : turns off all the devices in the list.
"""


class SmartHome:
    def __init__(self):
        self.devices = []

    def get_devices(self):
        return self.devices

    def get_device_at(self, index):
        return self.devices[index]

    def add_device(self, device):
        self.devices.append(device)

    def toggle_switch(self, index):
        self.devices[index].toggle_switch()

    def turn_on_all(self):
        for device in range(len(self.devices)):
            self.devices[device].set_switch_status(True)
            # output = "{} is on:".format(self.devices[device])
            # print(output)

    def turn_all_off(self):
        for device in range(len(self.devices)):
            self.devices[device].set_switch_status(False)

# methods needed for the challenge

    """
    remove_device : removes the device at the specified index from the list.
    add_device_v2 : adds a device to the list based on a predefined dictionary of devices.
    get_device_length : returns the length of the list of devices.
    get_devices_on_count : returns the number of devices that are currently switched on.
    str : returns a string representation of the SmartHome object.
    """
    def remove_device(self, index):
        self.devices.pop(index)

    def add_device_v2(self, new_device):
        if new_device in device_dic:
            self.devices.append(device_dic[new_device])
        else:
            print("Option not available!")

    def get_device_length(self):
        return len(self.devices)

    def get_devices_on_count(self):
        switched_on_devices = 0
        for device in self.devices:
            if device:
                switched_on_devices += 1
            else:
                switched_on_devices -= 1
                
            return switched_on_devices

    def __str__(self):
        output = "Your gadgets:\n"
        for device in self.devices:
            output = output + "{}\n".format(device)

        return output


def test_smart_home():
    smart_home = SmartHome()
    plug1 = SmartPlug()
    plug2 = SmartPlug()
    washing_machine = SmartWashingMachine()

    plug2.toggle_switch()
    plug2.set_consumption_rate(45)
    washing_machine.set_wash_mode_options("Eco")
    smart_home.add_device(plug1)
    smart_home.add_device(plug2)
    print(smart_home)
    smart_home.turn_on_all()
    print(smart_home)


test_smart_home()

