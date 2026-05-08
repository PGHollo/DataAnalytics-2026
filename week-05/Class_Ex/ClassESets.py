
states = {"New York", "Ohio", "Texas", "Florida", "Nevada"}

print(f"Total number of states: {len(states)}")

print(f"Is Texas in the set? {'Texas' in states}")

print(f"States in alphabetical order: {sorted(states)}")

longest_state = max(states, key=len)

print(f"Longest state name: {longest_state}")
print(f"Length of longest state name: {len(longest_state)} characters")

states.add("Georgia")
print(f"Updated set after adding Georgia: {states}")

states.discard("Florida")
print(f"Updated set after removing Florida: {states}")