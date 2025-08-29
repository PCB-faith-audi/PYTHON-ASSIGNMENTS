# The Base Class
class Plane:
    def move(self):
        print("A plane is moving in the sky...This is amazing!")

    def capacity(self):
        return "Capacity: Unknown"

    def speed(self):
        return "Speed: Unknown"


# The Derived Classes
class PassengerPlane(Plane):
    def move(self):
        print("🛫 The passenger plane is flying with hundreds of people onboard!")

    def capacity(self):
        return "Capacity: Around 400 passengers"

    def speed(self):
        return "Speed: 950 km/h"


class CargoPlane(Plane):
    def move(self):
        print("📦 The cargo plane is transporting goods across continents!")

    def capacity(self):
        return "Capacity: Up to 130 tons of cargo"

    def speed(self):
        return "Speed: 890 km/h"


class FighterJet(Plane):
    def move(self):
        print("⚔️ The fighter jet is soaring at supersonic speed!")

    def capacity(self):
        return "Capacity: 1–2 pilots only"

    def speed(self):
        return "Speed: 2,450 km/h (Mach 2)"


class Glider(Plane):
    def move(self):
        print("🪂 The glider is silently gliding using air currents!")

    def capacity(self):
        return "Capacity: 1–2 people"

    def speed(self):
        return "Speed: 300 km/h (no engine)"


# --- Testing Polymorphism ---
planes = [PassengerPlane(), CargoPlane(), FighterJet(), Glider()]

for p in planes:
    p.move()
    print(p.capacity())
    print(p.speed())
    print("--")
