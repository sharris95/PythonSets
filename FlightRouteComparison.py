#FlightRouteComparison

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
common_destinations = our_routes.intersection(competitor_routes)
print(f"Common Destinations: {common_destinations}")
unique_to_our_airline = our_routes.difference(competitor_routes)
print(f"Unique to Our Airline: {unique_to_our_airline}")
all_destinations = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK"}
neither_shared = all_destinations - (our_routes.union(competitor_routes))
print(f"Destinations neither airline shares: {neither_shared}")
