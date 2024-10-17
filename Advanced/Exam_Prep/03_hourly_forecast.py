def forecast(*locations):
    weather_priority = {
        "Sunny": 0,
        "Cloudy": 1,
        "Rainy": 2,
    }

    sorted_forecast = sorted(locations, key=lambda loc: (weather_priority[loc[1]], loc[0]) )

    final_print = [f"{location} - {weather}"  for location, weather in sorted_forecast]

    return '\n'.join(final_print)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))