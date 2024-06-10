from uagents import Agent
from utils import request_ride

class PassengerAgent(Agent):
    def __init__(self, name, location, destination):
        super().__init__(name=name)
        self.location = location
        self.destination = destination

    def request_ride(self):
        ride_request = request_ride(self.location, self.destination)
        return ride_request

# Example usage:
# passenger = PassengerAgent(name="Passenger1", location=(1, 1), destination=(5, 5))
