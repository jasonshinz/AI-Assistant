from machine import Pin, I2C
import ssd1306


class Display:
    WIDTH = 128
    HEIGHT = 64

    def __init__(self):
        self.i2c = I2C(
            0,
            scl=Pin(9),
            sda=Pin(8),
            freq=400000
        )

        self.oled = ssd1306.SSD1306_I2C(
            self.WIDTH,
            self.HEIGHT,
            self.i2c
        )

        self.clear()

    def clear(self):
        self.oled.fill(0)

    def text(self, message, x=0, y=0):
        self.oled.text(message, x, y)

    def show(self):
        self.oled.show()

    def center(self, message):
        self.oled.fill(0)

        x = max((128 - len(message) * 8) // 2, 0)
        y = 28

        self.oled.text(message, x, y)
        self.oled.show()
    
    def title(self, title):
        self.oled.fill(0)

        self.oled.text(title, 0, 0)

        self.oled.hline(0, 10, 128, 1)
    
    def message(self, msg):
        self.oled.text(msg, 0, 18)
        
    def status(self, status):
        self.oled.text(status, 0, 48)
    
    def weather(self, city, temperature, condition, updated):
        self.clear()

        self.title(city)

        self.oled.text(f"{temperature:.1f} C", 0, 18)

        self.oled.text(condition, 0, 32)

        self.oled.text(updated, 0, 48)

        self.show()