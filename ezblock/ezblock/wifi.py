from ezblock.basic import _Basic_class
from ezblock.utils import print, getIP
import time
# re-正则表达式
class WiFi(_Basic_class):
    message = """
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country={}
network={{
    ssid="{}"
    psk="{}"
    key_mgmt=WPA-PSK 
}}"""

    def __init__(self):
        self.country = ""

    def connect(self, ssid, psk):
        ip = getIP('wlan0')
        if ip:
            print('WiFi is already connected, skip')
            print("IP: %s" % ip)
            return True
        print("Connecting to \"{}\"...".format(ssid))
        message = self.message.format(self.country, ssid, psk)
        with open("/etc/wpa_supplicant/wpa_supplicant.conf", "w") as f:
            f.write(message)
        
        for i in range(6):
            if i != 0:
                print('Timeout, retry ({})...'.format(i))
            self.run_command("wpa_cli -i wlan0 reconfigure")
            time.sleep(1)
            time_start = time.time()
            while True:
                ip = getIP('wlan0')
                if ip:
                    print("IP: %s" % ip)
                    print('WiFi connect success')
                    return True

                time_end = time.time()
                if time_end-time_start > 10:
                    print('WiFi connect failed')
                    break 
                time.sleep(0.1)
        return False

    def write(self, country, ssid, psk):
        self.country = country
        self.connect(ssid, psk)

def test():
    WiFi().write("MakerStarsHall", "sunfounder", "CN")
if __name__ == "__main__":
    test()

