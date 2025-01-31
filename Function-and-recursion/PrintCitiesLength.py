cities = ["Dhaka", "Chittagong","Cumilla", "Barishal", "Khulna"]

def print_length(cities):
  ln = 0
  for city in cities:
    ln += 1
  return ln

print(print_length(cities))

def print_list(cities):
  for city in cities:
    print(city, end=" ")

print_list(cities)
print()