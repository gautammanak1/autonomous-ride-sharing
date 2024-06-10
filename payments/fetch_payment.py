from fetchai.ledger.api import LedgerApi
from fetchai.ledger.crypto import Entity

def process_payment(fare, passenger_wallet, driver_wallet):
    api = LedgerApi('127.0.0.1', 8100)
    passenger_entity = Entity(passenger_wallet)
    driver_entity = Entity(driver_wallet)

    tx = api.tokens.transfer(passenger_entity, driver_entity, fare, 100)
    api.sync([tx])

# Example usage:
# process_payment(15, 'passenger_private_key', 'driver_private_key')
