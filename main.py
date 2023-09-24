from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import utime
import freesans20
import writer

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

WIDTH  = 128                                          
HEIGHT = 64                                             

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    t = 27 - (reading - 0.706) / 0.001721
    oled.fill(0)

    formatted_temperature = "{:.1f}".format(t)

    font_writer = writer.Writer(oled, freesans20)

    font_writer.set_textpos(44, 0)
    font_writer.printstring("Case")

    font_writer.set_textpos(8, 20)
    font_writer.printstring("Temperature")

    font_writer.set_textpos(46, 44)
    font_writer.printstring(str(formatted_temperature))

    font_writer.set_textpos(68, 44)
    font_writer.printstring("C")
    oled.show()
    
    # Delay for 5 seconds
    utime.sleep(3)
    oled.fill(0)

    # Display another text after the delay
    font_writer.set_textpos(40, 8)
    font_writer.printstring("ASRI")
    
    font_writer.set_textpos(8, 38)
    font_writer.printstring("RUSLAN-PC")
    oled.show()
    
    # Delay for 5 seconds again
    utime.sleep(3)

