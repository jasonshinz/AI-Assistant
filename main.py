import time

from config import WIFI_SSID, WIFI_PASSWORD
from display import Display
from time_service import TimeService
from weather import Weather
from wifi import WiFi


display = Display()
wifi = WiFi(WIFI_SSID, WIFI_PASSWORD)
weather = Weather()
clock = TimeService()


display.title("AI Assistant")
display.message("Connecting WiFi...")
display.show()

if not wifi.connect():
    display.clear()
    display.title("WiFi")
    display.message("Connection Failed")
    display.show()
    raise Exception("WiFi connection failed")


while True:

    try:
        display.clear()
        display.title("Weather")
        display.message("Updating...")
        display.show()

        weather.update()

        display.weather(
            city="Wellington",
            temperature=weather.temperature(),
            condition=weather.condition(),
            updated=clock.now()
        )

    except Exception as e:
        print(e)

        display.clear()
        display.title("Weather")
        display.message("Update Failed")
        display.show()

    time.sleep(60)