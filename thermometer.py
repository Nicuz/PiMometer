#-*- coding: utf-8 -*-
import Adafruit_DHT, locale
from Adafruit_CharLCD import Adafruit_CharLCD
from time import strftime, sleep

#Italian localization
locale.setlocale(locale.LC_TIME, "it_IT")

#PIN
lcd_rs        = 7
lcd_en        = 8
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4
lcd_columns   = 16
lcd_rows      = 2

#Display initialization
lcd = Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

#DHT11
sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#Function to display text on the HD44780
def text_on_display():
        #Time and date on first row
        lcd.message(strftime("%H:%M %a %d %b\n"))

        #Thermometer icon
        thermometer_icon = [0x04,0x0a,0x0a,0x0e,0x0e,0x1f,0x1f,0x0e]
        lcd.create_char(0, thermometer_icon)

        #Degree circle icon
        degree_circle_icon = [0x0e,0x0a,0x0e,0x00,0x00,0x00,0x00,0x00]
        lcd.create_char(1, degree_circle_icon)

        #Water drop icon
        water_drop_icon = [0x04,0x04,0x0a,0x0a,0x11,0x11,0x11,0x0e]
        lcd.create_char(2, water_drop_icon)

        #Temperature and humidity on second row
        lcd.message("\n\x00 {0:0.1f}\x01C \x02 {1:0.1f}%".format(temperature, humidity))

#Print data on display after startup
text_on_display()

#Data update
while True:
        #Check how many seconds are missing at the next minute, useful to update the display everytime the time changes
        sleep(60-int(strftime("%S")))

        #Update temperature and himidity
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        #Clear text
        lcd.clear()

        #Update text on display
        text_on_display()
