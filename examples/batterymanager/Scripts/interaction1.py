# noinspection PyUnusedLocal
import time

class Device:
    def __init__(self, device_id):
        self.id = device_id

    def shell(self, command):
        # Simulate the shell method for illustration purposes
        print(f"Running command: {command}")

    def current_activity(self):
        # Simulate the current_activity method for illustration purposes
        return "com.google.android.apps.chrome.Main"  # Replace with the actual implementation

def open_chrome_canary(device, url: str, sleep=5) -> None:
    # Assuming the package name for Chrome Canary is 'com.chrome.canary'
    chrome_canary_package_name = 'com.chrome.canary'

    # Launch Chrome Canary with the specified URL
    device.shell(f'am start -a android.intent.action.VIEW -d {url} -n {chrome_canary_package_name}/com.google.android.apps.chrome.Main')

    # Wait for the browser to load (adjust sleep time as needed)
    time.sleep(sleep)

def main(device, *args, **kwargs) -> None:
    print('=INTERACTION=')
    print(device.id)
    print(device.current_activity())

    # List of URLs to open
     urls_to_open = [
    "https://playground.babylonjs.com/#I6AR8X",
    "https://playground.babylonjs.com/#Y3C0HQ#146",
    "https://playground.babylonjs.com/#N96NXC#106",
    "https://playground.babylonjs.com/#YEZPVT",
    "https://playground.babylonjs.com/#N96NXC#106",
    "https://playground.babylonjs.com/#4QH8JM",
    "https://playground.babylonjs.com/#YCY2IL#9",
    "https://playground.babylonjs.com/#L92PHY#217",
    "https://playground.babylonjs.com/#9K3MRA#2",
    "https://playground.babylonjs.com/#PIZ1GK#1116",
    "https://playground.babylonjs.com/#IQN716#9",
    "https://playground.babylonjs.com/#CBGEQX#858",
    "https://playground.babylonjs.com/#7V0Y1I#1",
    "https://playground.babylonjs.com/#9WUJN#12",
    "https://playground.babylonjs.com/#20OAV9#16",
    "https://playground.babylonjs.com/#20OAV9#325",
    "https://playground.babylonjs.com/#20OAV9#8",
    "https://playground.babylonjs.com/#20OAV9#1",
    "https://playground.babylonjs.com/#5T8G3I#16",
    "https://playground.babylonjs.com/#7CBW04",
    "https://playground.babylonjs.com/#WGZLGJ",
    "https://playground.babylonjs.com/#ABDDD6#1",
    "https://playground.babylonjs.com/#JUKXQD",
    "https://playground.babylonjs.com/#7G0IQW",
    "https://playground.babylonjs.com/#FEEK7G#116",
    "https://playground.babylonjs.com/#G3HSAW#",
    "https://playground.babylonjs.com/#20OAV9#15",
    "https://toji.github.io/webgpu-test/"
    ]

    # Open each URL in Chrome Canary
    for index, url in enumerate(urls_to_open, start=1):
        print(f"Opening URL {index}: {url}")
        open_chrome_canary(device, url)

        # You may adjust the sleep time or add additional logic here if needed
        time.sleep(10)  # Wait for 10 seconds between each URL

if __name__ == "__main__":
    # Create a Device object (replace this with your actual Device class instantiation)
    my_device = Device(device_id="pixel5g")

    # Call the main function with the Device object
    main(my_device)

