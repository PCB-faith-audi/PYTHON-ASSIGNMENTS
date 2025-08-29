#  this is the base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"
    
    def power_on(self):
        return f"{self.device_info()} is powering ON..."
    
    def power_off(self):
        return f"{self.device_info()} is shutting down..."


# The Derived Class (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call parent constructor
        super().__init__(brand, model)
        self.storage = storage  # in GB
        self.battery = battery  # in mAh
    
    # The encapsulation part(using getter and setter for battery)
    def get_battery(self):
        return f"Battery: {self.battery} mAh"
    
    def set_battery(self, new_capacity):
        if new_capacity > 0:
            self.battery = new_capacity
        else:
            print("Invalid battery capacity!")

    # The polymorphism part(overriding parent method)
    def device_info(self):
        return f"{self.brand} {self.model} | {self.storage}GB Storage | {self.battery}mAh Battery"
    
    def take_photo(self):
        return f"{self.device_info()} is taking a photo 📸"
    
    def make_call(self, number):
        return f"Calling {number} from {self.device_info()}..."


# Another derived class
class SmartWatch(Device):
    def __init__(self, brand, model, strap_color):
        super().__init__(brand, model)
        self.strap_color = strap_color

    # Polymorphism: overriding device_info
    def device_info(self):
        return f"{self.brand} {self.model} | Strap Color: {self.strap_color}"
    
    def track_steps(self, steps):
        return f"{self.device_info()} tracked {steps} steps today 👣"


# --- Testing our classes ---
phone = Smartphone("Samsung", "Galaxy S24", 256, 5000)
watch = SmartWatch("Apple", "Watch Series 9", "Black")

print(phone.power_on())
print(phone.take_photo())
print(phone.make_call("+254712345678"))
print(phone.get_battery())
phone.set_battery(6000)
print(phone.get_battery())
print(phone.device_info())

print("\n---\n")

print(watch.power_on())
print(watch.track_steps(8000))
print(watch.device_info())
