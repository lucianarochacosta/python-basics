city = {"name": "Sao Paulo", "state": "Sao Paulo", "pop_million": 12.2}

for key in city:
    print(f"{key}: {city[key]}")

for position in range(len(city)):
    city[position] = "Rio de Janeiro"
print(city)

print(list(range(10)))
print(list(range(2, 10)))
print(list(range(2, 10, 2)))