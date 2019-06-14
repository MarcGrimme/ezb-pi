from ezblock.pin import Pin
from ezblock.led import LED
from ezblock.pwm import PWM
from ezblock.servo import Servo
from ezblock.signal import Signal
from ezblock.spi import SPI
from ezblock.switch import Switch
from ezblock.uart import UART
from ezblock.i2c import I2C
from ezblock.adc import ADC
from ezblock.ble import BLE
from ezblock.ble import Remote
from ezblock.music import Music
from ezblock.color import Color
from ezblock.camera import Camera
from ezblock.iot import IOT
from ezblock.tts import TTS
from ezblock.irq import IRQ
from ezblock.wifi import WiFi
from ezblock.utils import *
from ezblock.taskmgr import Taskmgr
from ezblock.modules import *
from ezblock.send_email import SendMail

def __reset_mcu__():
    mcurst = Pin("MCURST")
    mcurst.on()
    delay(1)
    mcurst.off()

def __main__():
    import sys

    usage = '''
Usage:
    sudo python3 install.py [option]

Options:
    reset-mcu   Reset MCU on Ezblock
    -h          Show this help text and exit
'''
    option = ""
    if len(sys.argv) > 1:
        option = sys.argv[1]
    if "-h" == option:
        print(usage)
        quit()
    elif option == "reset-mcu":
        __reset_mcu__()
    else:
        print(usage)
        quit()
    