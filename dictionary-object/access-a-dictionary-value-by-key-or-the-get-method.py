flight_prices = {
    "Chicago": 199,
    "San Francisco": 499,
    "Denver": 295
}

# Keys are case sensitive
print(flight_prices["Chicago"])
print(flight_prices["Denver"])
print(flight_prices["San Francisco"])

gym_memberships = {
    29: ["Machines"],
    49: ["Machines", "Vitamin Supplements"],
    79: [ "Machines", "Vitamin Supplements", "Sauna" ]
}

print(gym_memberships[49])

print(gym_memberships.get(29, ["Basic Package"]))
print(gym_memberships.get(200))