# noinspection PyUnusedLocal
import time
from AndroidRunner.Devices import Device

def open_chrome_canary(device:Device, url: str) -> None:
    
    chrome_canary_package_name = 'com.chrome.canary'

    # Launch Chrome Canary with the specified URL
    device.shell(f'am start -a android.intent.action.VIEW -d {url} -n "chrome_canary_package_name/com.google.android.apps.chrome.Main"')

    time.sleep(120)
    #device.shell(f'am force-stop {chrome_canary_package_name}')

def swip(device:Device, x1, y1，x2, y2)-> None:
    device.shell('input swip %s %s %s %s' % (x1, y1，x2, y2))
    time.sleep(2)

def tap(device:Device, x, y) -> None:
    tap_command = f'input tap {x} {y}'
    print(f'Tapping at coordinates: {tap_command}')
    device.shell(tap_command)
    time.sleep(2)


def main(device:Device, *args, **kwargs) -> None:
    print('=INTERACTION=')
    print((device.id))
    print((device.current_activity()))

    # List of URLs to open
    urls_to_open = [
    "https://playground.babylonjs.com/#I6AR8X",  
    ]

    # Open each URL in Chrome Canary
    for index, url in enumerate(urls_to_open, start=0):
        print(f"Opening URL: {url}")
        open_chrome_canary(device, url)
	#time.sleep(2)
        #tap(device, 44, 383)
        #tap(device, 160, 1192)
        #tap(device, 640, 1040)
        #time.sleep(10)
        swip(device, 100, 700, 1000 ,700)
        time.sleep(3)
        swip(device, 1000, 700, 100, 700)# specific coordinate in your device from right to left
        time.sleep(3)
        swip(device, 500, 100, 500 ,1000)
        time.sleep(3)
        swip(device, 500, 1000, 500, 100）
	time.sleep(10)

       # time.sleep(3)  # Wait for 4 seconds between each URL
        device.shell(f'am force-stop {chrome_canary_package_name}') # break
    print('a')
    
    

if __name__ == "__main__":
    # Create a Device object (replace this with your actual Device class instantiation)
    Device="pixel5g"
    my_device = "pixel5g"

    # Call the main function with the Device object
    main(my_device)

