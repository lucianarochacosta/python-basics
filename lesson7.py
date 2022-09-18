city_data = {"name": "Paris", "country": "France", "num_hab": 2161000.0}
print(type(city_data))

city_data["area_km2"] = 105.4
print(city_data)

print(city_data["country"])

city_data2 = city_data.copy()
city_data2["area_km2"] = 105
print(city_data2)
print(city_data)

new_data = {"year_foundation": 1792}
city_data2.update(new_data)
print(city_data2)

print(city_data.get("mayor"))

print(city_data.keys()) # retorna uma lista de chaves de um dicionario
print(city_data.values()) # retorna uma lista de valores de um dicionario
print(city_data.items()) # retorna uma lista de tuplas (chave, valor) de um dicionario