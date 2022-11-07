import requests

API = "70bf3642aa2f2b86f74a7ce5bc8d96c3"
city = input("Anna kaupungin nimi: ")
geocode = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API}"
geodata = requests.get(geocode).json()

try:
    city_name = geodata[0]["local_names"]["fi"]
except KeyError:
    city = geodata[0]["name"]

latitude = geodata[0]["lat"]
longitude = geodata[0]["lon"]
weather_query = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API}&units=metric&lang=fi"
weather_data = requests.get(weather_query).json()
celsius = weather_data["main"]["temp"]
fahrenheit = (celsius * 9/5) + 32

print(f'Kaupunki: {city}'
      f'\n{weather_data["weather"][0]["description"]}'
      f'\n{celsius} celsius astetta'
      f'\n{fahrenheit:.2f} fahrenheit astetta')