# noinspection PyUnusedLocal
import time
from AndroidRunner.Devices import Device

def open_chrome_canary(device:Device, url: str) -> None:
    
    chrome_canary_package_name = 'com.chrome.canary'

    # Launch Chrome Canary with the specified URL
    device.shell(f'am start -a android.intent.action.VIEW -d {url} -n "chrome_canary_package_name/com.google.android.apps.chrome.Main"')

    time.sleep(10)
    #device.shell(f'am force-stop {chrome_canary_package_name}')

#def swip(device:Device, x, y)-> None:
    #device.shell('input swip %s %s %s %s' % (x, y,x+1,y+1))
    #time.sleep(2)

def tap(device:Device, x, y) -> None:
    tap_command = f'input tap {x} {y}'
    print(f'Tapping at coordinates: {tap_command}')
    device.shell(tap_command)
    time.sleep(2)


def main(device: Device, *args, **kwargs) -> None:
    print('=INTERACTION=')
    print(device.id)
    print(device.current_activity())

    # List of URLs to open
    urls_to_open = [
        "https://playground.babylonjs.com/#I6AR8X",
        "https://playground.babylonjs.com/#Y3C0HQ#146",
    ]

    # Open each URL in Chrome Canary
    for index, url in enumerate(urls_to_open, start=0):
        print(f"Opening URL{index}: {url}")

        # Add a condition to skip the rest of the loop and go to the next iteration
        #if "babylon" in url:
        #    print("fnishied")
        #    continue

        open_chrome_canary(device, url)
        # Rest of your loop code


      
    # Rest of your loop code

         
	#time.sleep(2)
         # tap(device, 44, 383)
         # tap(device, 160, 1192)
        #  tap(device, 640, 1040)
        
        #swip(device, 100, 500)
       # time.sleep(2)
       # swip(device, 500, 100)

       # time.sleep(3)  # Wait for 4 seconds between each URL
    print('a')
    
    

if __name__ == "__main__":
    # Create a Device object (replace this with your actual Device class instantiation)
    Device="pixel5g"
    my_device = "pixel5g"

    # Call the main function with the Device object
    main(my_device)

