from http_client import HttpClient


class Weather:

    URL = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=-41.2865"
        "&longitude=174.7762"
        "&current=temperature_2m,weather_code"
    )

    def __init__(self):
        self.client = HttpClient()
        self.data = None

    def update(self):
        self.data = self.client.get_json(self.URL)

    def temperature(self):
        return self.data["current"]["temperature_2m"]

    def weather_code(self):
        return self.data["current"]["weather_code"]

    def condition(self):
        code = self.weather_code()

        conditions = {
            0: "Clear",
            1: "Mainly Clear",
            2: "Partly Cloudy",
            3: "Cloudy",
            45: "Fog",
            61: "Rain",
            63: "Rain",
            65: "Heavy Rain",
            71: "Snow",
            80: "Showers",
            95: "Thunderstorm"
        }

        return conditions.get(code, f"Code {code}")