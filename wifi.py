import network
import time


class WiFi:

    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)

    def connect(self):
        if self.wlan.isconnected():
            return True

        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)

        print("Connecting...")

        timeout = 10

        while timeout > 0:

            if self.wlan.isconnected():
                print("Connected")
                print(self.wlan.ifconfig())
                return True

            timeout -= 1
            time.sleep(1)

        return False

    def ip(self):
        if self.wlan.isconnected():
            return self.wlan.ifconfig()[0]

        return None