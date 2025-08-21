# Weather Model Program

def quadratic_weather_model(hour):
    """
    Simple quadratic temperature model:
    - highest at 12 hrs (30°C)
    - cooler at night/morning
    """
    temp = -0.1 * (hour - 12) ** 2 + 30
    return round(temp, 2)


# if _ _name_ _== "_ _main_ _":
    for h in [0, 6, 12, 18, 23]:
        print(f"At {h}:00, temperature = {quadratic_weather_model(h)}°C")
