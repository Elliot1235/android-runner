# noinspection PyUnusedLocal
import time
from AndroidRunner.Devices import Device

def open_chrome_canary(device:Device, url: str) -> None:
    
    chrome_canary_package_name = 'com.chrome.canary'

    # Launch Chrome Canary with the specified URL
    device.shell(f'am start -a android.intent.action.VIEW -d {url} -n {chrome_canary_package_name}/com.google.android.apps.chrome.Main')

    # Wait for the browser to load (adjust sleep time as needed)
    time.sleep(10)
    #device.shell(f'am force-stop {chrome_canary_package_name}')

def tap(device, x, y)-> None:
    device.shell('input tap %s %s' %(x, y))
    time.sleep(2)
def tap(device:Device, x, y) -> None:
    tap_command = f'input tap {x} {y}'
    print(f'Tapping at coordinates: {tap_command}')
    device.shell(tap_command)
    time.sleep(2)


def main(device:Device, *args, **kwargs) -> None:
    print('=INTERACTION=')
   # print((device.id))
    print((device.current_activity()))

    # List of URLs to open
    urls_to_open = [
    #"https://playground.babylonjs.com/#I6AR8X", #1
    "https://playground.babylonjs.com/#Y3C0HQ#146", #2
    "https://playground.babylonjs.com/#N96NXC#106", #3
    "https://playground.babylonjs.com/#YEZPVT", #4
    "https://playground.babylonjs.com/#XMEL56#7", #5
    "https://playground.babylonjs.com/#4QH8JM", #6
    "https://playground.babylonjs.com/#YCY2IL#9", #7
    "https://playground.babylonjs.com/#L92PHY#217", #8
    "https://playground.babylonjs.com/#9K3MRA#2", #9
    "https://playground.babylonjs.com/#PIZ1GK#1116", #10
    "https://playground.babylonjs.com/#IQN716#9",
    "https://playground.babylonjs.com/#CBGEQX#858",
    "https://playground.babylonjs.com/#7V0Y1I#1",
    "https://playground.babylonjs.com/#9WUJN#12",
    "https://playground.babylonjs.com/#20OAV9#16",
    "https://playground.babylonjs.com/#20OAV9#325",
    "https://playground.babylonjs.com/#WGZLGJ",
    "https://playground.babylonjs.com/#20OAV9#8",
    "https://playground.babylonjs.com/#20OAV9#1",
    "https://playground.babylonjs.com/#5T8G3I#16", #20

    "https://playground.babylonjs.com/#7CBW04",
    "https://playground.babylonjs.com/#ABDDD6#1",
    "https://playground.babylonjs.com/#JUKXQD",
    #"https://playground.babylonjs.com/#7G0IQW",
    #"https://playground.babylonjs.com/#FEEK7G#116", #25
    #"https://playground.babylonjs.com/#G3HSAW#",
    #"https://playground.babylonjs.com/#20OAV9#15",
    #"https://playground.babylonjs.com/#2SA7J8#7",
    #"https://playground.babylonjs.com/#G3HSAW#6",
    #"https://playground.babylonjs.com/#BH23ZD#1" #30
    ]

    # Open each URL in Chrome Canary
    for index, url in enumerate(urls_to_open, start=1):
        print(f"Opening URL: {url}")
        open_chrome_canary(device, url)
        #time.sleep(2)
        tap(device, 44, 383)
        tap(device, 160, 1192)
        tap(device, 640, 1040)
        # You may adjust the sleep time or add additional logic here if needed
        #time.sleep(120)  # Wait for 4 seconds between each URL
        #device.shell(f'am force-stop {chrome_canary_package_name}')
    print('a')
    
    

if __name__ == "__main__":
    # Create a Device object (replace this with your actual Device class instantiation)
    Device="pixel5g"
    my_device = "pixel5g"

    # Call the main function with the Device object
    main(my_device)

