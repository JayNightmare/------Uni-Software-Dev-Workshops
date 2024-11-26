import requests

STOP_CODE = '490006412E2'
TFL_API_URL = f'https://api.tfl.gov.uk/StopPoint/{STOP_CODE}/arrivals'

def can_catch_bus(walk_time_minutes=12):
    try:
        response = requests.get(TFL_API_URL)
        response.raise_for_status()  # Raise error for bad HTTP responses (4xx or 5xx)
        buses = response.json()

        bus_57_arrivals = [bus for bus in buses if bus['lineId'] == '57']

        if not bus_57_arrivals:
            print("No 57 buses available at this time.")
            return

        # Sort buses by arrival time (in seconds)
        bus_57_arrivals.sort(key=lambda bus: bus['timeToStation'])

        # Get the first bus arrival
        next_bus = bus_57_arrivals[0]
        arrival_time_minutes = next_bus['timeToStation'] // 60  # Convert seconds to minutes

        print(f"Next 57 bus arrives in {arrival_time_minutes} minutes.")
        if arrival_time_minutes <= walk_time_minutes:
            print("You can catch the bus!")
        else:
            print("You will miss the bus.")

        if len(bus_57_arrivals) > 1:
            print("Other upcoming 57 buses:")
            for bus in bus_57_arrivals[1:]:
                print(f"- Arrives in {bus['timeToStation'] // 60} minutes.")
    except requests.exceptions.RequestException as err:
        print(f"Error fetching bus data: {err}")
    except KeyError as err:
        print(f"Unexpected response structure: {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

can_catch_bus(12)
