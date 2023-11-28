# noinspection PyUnusedLocal
import time
from AndroidRunner.Devices import Device

def tap(device:Device, x, y) -> None:
    tap_command = f'input tap {x} {y}'
    print(f'Tapping at coordinates: {tap_command}')
    device.shell(tap_command)
    time.sleep(2)

def main(device: Device, *args, **kwargs) -> None:
    print('=INTERACTION=')
    print(device.current_activity())

    # List of URLs to open
    device.shell(f'am start -a android.intent.action.VIEW -d https://playground.babylonjs.com/#7CBW04 -n "com.chrome.canary/com.google.android.apps.chrome.Main"')
    time.sleep(10)
    tap(device, 44, 383)
    tap(device, 160, 1192)
    tap(device, 640, 1040)
    time.sleep(110)
        
    swip(device, 100, 500)
    time.sleep(2)
    swip(device, 500, 100)

       # time.sleep(3)  # Wait for 4 seconds between each URL
    print('a')
    
    

if __name__ == "__main__":
    # Create a Device object (replace this with your actual Device class instantiation)
    Device="pixel5g"
    my_device = "pixel5g"

    # Call the main function with the Device object
    main(my_device)

