# Vacuum Cleaner Problem

rooms = {"A": "Dirty", "B": "Dirty"}
location = "A"

print("Initial State:", rooms)

while "Dirty" in rooms.values():
    if rooms[location] == "Dirty":
        print("Cleaning Room", location)
        rooms[location] = "Clean"
    else:
        print("Moving to next room")
        location = "B" if location == "A" else "A"

print("Final State:", rooms)
