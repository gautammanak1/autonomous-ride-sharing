from agents.driver import DriverAgent
from agents.passenger import PassengerAgent
from payments.fetch_payment.py import process_payment
from simulation.traffic_simulation import simulate_traffic, optimize_ride_distribution

def main():
    # Initialize agents
    driver = DriverAgent(name="Driver1", location=(0, 0))
    passenger = PassengerAgent(name="Passenger1", location=(1, 1), destination=(5, 5))

    # Passenger requests a ride
    ride_request = passenger.request_ride()
    
    # Driver handles the ride request
    ride_details = driver.handle_request(ride_request)
    
    # Process payment
    fare = ride_details['fare']
    process_payment(fare, 'passenger_private_key', 'driver_private_key')
    
    # Simulate traffic and optimize ride distribution
    traffic_data = simulate_traffic()
    optimized_distribution = optimize_ride_distribution(traffic_data)
    
    print(f"Ride details: {ride_details}")
    print(f"Optimized distribution: {optimized_distribution}")

if __name__ == "__main__":
    main()
