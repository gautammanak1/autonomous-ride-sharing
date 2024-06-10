from uagents import Agent
from utils import negotiate_fare, schedule_ride, optimize_route

class DriverAgent(Agent):
    def __init__(self, name, location):
        super().__init__(name=name)
        self.location = location

    def handle_request(self, request):
        fare = negotiate_fare(request)
        ride_details = schedule_ride(request, self.location, fare)
        optimized_route = optimize_route(ride_details)
        return optimized_route

# Example usage:
# driver = DriverAgent(name="Driver1", location=(0, 0))
