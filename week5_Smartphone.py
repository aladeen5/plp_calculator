# smartphone.py

# Base class
class Device:
    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        print(f"{self.brand} device is powering on...")

# Derived class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand)  # Call base class constructor
        self.model = model
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        print(f"📱 Calling {number} from {self.brand} {self.model}...")

    def check_battery(self):
        print(f"🔋 Battery level: {self.battery}%")

    def upgrade_storage(self, new_storage):
        if new_storage > self.storage:
            self.storage = new_storage
            print(f"💾 Storage upgraded to {self.storage}GB!")
        else:
            print("⚠️ New storage must be greater than current storage.")

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S24", 128, 85)
phone2 = Smartphone("Apple", "iPhone 15", 256, 60)

# Use methods
phone1.power_on()
phone1.make_call("+254700123456")
phone1.check_battery()
phone1.upgrade_storage(256)

phone2.power_on()
phone2.check_battery()
