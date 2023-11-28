[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=S2-group_android-runner&metric=alert_status)](https://sonarcloud.io/dashboard?id=S2-group_android-runner)
[![Build Status](https://travis-ci.org/S2-group/android-runner.svg?branch=master)](https://travis-ci.org/S2-group/android-runner)
[![Coverage Status](https://coveralls.io/repos/github/S2-group/android-runner/badge.svg?branch=master)](https://coveralls.io/github/S2-group/android-runner?branch=master&service=github)
# Android Runner
Android Runner (AR) is a tool for automatically executing measurement-based experiments on native and web apps running on Android devices.

The following scientific publication gives an overview about the main components, plugins, and configurations of Android Runner (as of 2020): [A-Mobile 2020 publication](https://github.com/S2-group/android-runner/blob/master/documentation/A_Mobile_2020.pdf)  

A complete tutorial on how to use Android Runner is available in the following YouTube playlist: [Android Runner Tutorials](https://www.youtube.com/watch?v=-ZXT176ljjI&list=PLLbZZOioDh3P50WcYbuBMZEJokJH3ZONr).

As visualized below, Android Runner consists of the following components:
- **Experiment orchestrator**: Is in charge of executing the whole experiment according to the experiment configuration provided by the user.
- **Devices manager**: Is responsible for providing a layer of abstraction on the low-level operations involving the Android devices.
- **Progress manager**: Keeps track of the execution of each run of the experiment.
- **Plugin handler**: Provides a set of facilities for managing the profilers and an extension point that third-party developers can use for integrating their own measurement tools into Android Runner.

<p align="center">
<img src="./documentation/overview.jpg" alt="Overview of Android Runner" width="500"/>
</p>

# Table of Contents
- [The virtual environment](#the-virtual-environment)
- [Quick Start](#quick-start)
- [Methods to detect energy consumption](#methods-to-detect-energy-consumption)
- [Methods to detect performance](#methods-to-detect-performance)
- [Methods to open the subjects automatically](#methods-to-open-the-subjects-automatically)
  - [tap function](#tap-function)
  - [swip function](#swip-function)
- [Experiment Continuation](#experiment-continuation)
- [Turn off charging function](#turn-off-charging-function)
- [Compatible Devices](#compatible-devices)


## The virtual environment
 ```activate way
 python -m venv kim #create the virtual environment called kim
 cd ～   #to the package where you create the virtual environment
 source kim/bin/activate  #activate your virtual environment 
 ```

## Quick Start
To run an experiment, run:
```bash
python3 android-runner path_to_your_config.json
```
Example configuration files can be found in the subdirectories of the `examples` directory.

To run an experiment to detect the performance run:
```bash
python3 android-runner android-runner/examples/performance/config.json
```

## Methods to imitate human hands to automatically click screen and move the screen
### tap
Create the tap function in the interaction.py to auctomatically click the screen to change the API from WebGL to WebGPU
```interaction.py

def tap(device:Device, x, y) -> None:  # x is the abscissa y is the ordinate
    tap_command = f'input tap {x} {y}'
    print(f'Tapping at coordinates: {tap_command}')
    device.shell(tap_command)
    time.sleep(2)
```

### swip
Create the swip function in the interaction.py to auctomatically move the screen from one specific coordinate to another

```interaction.py
def swip(device:Device, x1, y1, x2, y2)-> None:
    #device.shell('input swip %s %s %s %s' % (x1,y1,x2,y2))  # x1, y1: Starting coordinates of the swipe. x2, y2: Ending coordinates of the swipe.
    #time.sleep(2)
```

## Methods to open the subjects automatically
Step1. Create the function to open the specific  browser and the URL in the interaction.py

```interaction.py
def open_chrome_canary(device:Device, url: str) -> None:
    chrome_canary_package_name = 'com.chrome.canary'
    device.shell(f'am start -a android.intent.action.VIEW -d {url} -n "chrome_canary_package_name/com.google.android.apps.chrome.Main"')
    time.sleep(120) #Each website runs for 120 seconds
def main(device:Device, *args, **kwargs) -> None:
    urls_to_open = [
    "https://playground.babylonjs.com/#I6AR8X"      # URLs to open the subjects(30)
    ]
    # Open each URL in Chrome Canary
    for index, url in enumerate(urls_to_open, start=0):
        print(f"Opening URL: {url}")
        open_chrome_canary(device, URL)
        tap(device, 44, 383)
        tap(device, 160, 1192)
        tap(device, 640, 1040) # specific coordinate in your device
        time.sleep(3)
        swip(device, 100, 700, 1000 ,700)
        time.sleep(3)
        swip(device, 1000, 700, 100, 700)# specific coordinate in your device from right to left
        time.sleep(3)
        swip(device, 500, 100, 500 ,1000)
        time.sleep(3)
        swip(device, 500, 1000, 500, 100)# specific coordinate in your device from down to up

```
Step2. Add the interaction.py into the config.json

```config.json
 "interaction": [
      {
        "type": "python3",
        "path": "Scripts/interaction.py"
      }
    ],
```


## Methods to detect energy consumption
We used “Batterymanager” to detect the energy consumption
Step1： Download the apk（(https://github.com/S2-group/batterymanager-companion/releases)）
Step2:  Use adb commands install the application in the Android device

```
adb device  #check the connection
adb install <path to the apk>

```
Step3:  Run the config.json to detect and save the data
```bash
python3 android-runner android-runner/examples/batterymanager/config.json
```
## Methods to detect the performance
Based on the given performance plugin（https://github.com/S2-group/android-runner/blob/master/AndroidRunner/Plugins/android/Android.py）
two adb statements are added to obtain data on GPU memory usage and CPU Clock speed.

```GPU Memory Usage
def get_gpu_memory_usage(device, package_name):
        GPU_mem_u=device.shell(f"dumpsys gfxinfo {package_name} | grep -A1 'Total GPU memory usage:'")
        res = GPU_mem_u.split(',')[1].strip()
        return res

```


```CPU Clock Speed
def get_cpu_clockspeed(device):
        CPU_clock=device.shell(f'cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq')
        return CPU_clock

```
Run the config.json to detect and save the data
```bash
python3 android-runner android-runner/examples/performance/config.json
```
**scripts** *JSON*
A JSON list of types and paths of scripts to run. Below is an example:
```js
"scripts": {
  "before_experiment": "before_experiment.py",
  "before_run": "before_run.py",
  "interaction": "interaction.py",
  "after_run": "after_run.py",
  "after_experiment": "after_experiment.py"
}
```
Below are the supported types:
- **before_experiment**
  executes once before the first run
- **before_run**
  executes before every run
- **after_launch**
  executes after the target app/website is launched, but before profiling starts
- **interaction**
  executes between the start and end of a run
- **before_close**
  executes before the target app/website is closed
- **after_run**
  executes after a run completes
- **after_experiment**
  executes once after the last run
- Within the JSON object you can use `"type"` to `"python3"`, `"monkeyrunner"` or, `"monkeyreplay"` depending on the type of script.
  - `"python3"` can be used for a standard python script,
  - `"monkeyreplay"` for running a Monkeyrunner script with the use of the Monkeyrunner framework and 
  - `"monkeyrunner"` can be used to run a Monkeyrunner directly without the entire Monkeyrunner framework. 
- The `"timeout"` option is to set a maximum run time in miliseconds for the specified script. 
- The optional option `"logcat_regex"` filters the logcat messages such that it only keeps lines where the log message matches "\<expr\>" where "\<expr\>" is a regular expression.

## Experiment Continuation
In case of an error or a user abort during experiment execution, it is possible to continue the experiment if desired. This is possible by using a ```--progress``` tag with the starting command. For example:

```python3 android_runner your_config.json --progress path/to/progress.xml```

## Turn off charging function
During the test, in order to avoid data errors caused by charging, it is necessary to connect the USB and turn off the charging function.
There are two ways to operate: 
1. You can connect the USB cable for power supply and communication independently, and turn off charging before the experiment by modifying the developer options on the phone.
2. The USB charging function can be turned off through commands without affecting the communication function.

```
adb shell "echo 1 > /sys/class/power_supply/battery/input_suspend"

```
When input_suspend is 1, USB charging is disabled, and the current is found to be 0 using a USB monitor;
When input_suspend is 0, USB charging is normal.
Note: This flag will be restored to 0 after Android restarts.

## Compatible Devices
The table below shows on which mobile devices Android Runner and its profilers were tested and whether there are any known issues.

| Device/Profiler             	| Trepn                                                	| BatteryStats 	| Perfetto*      	|
|-----------------------------	|------------------------------------------------------	|--------------	|----------------	|
| LG Nexus 5X (Android 8.1.0) 	| No, energy consumption measurements always return 0. 	| Yes          	| N/A 	|
| Samsung Galaxy J7 Duo       	| No, energy consumption measurements always return 0. 	| Yes          	| N/A 	|
| Google Pixel 3              	| No, energy consumption measurements always return 0. 	| Yes          	| Yes            	|
| Google Pixel 5G             	| No, energy consumption measurements always return 0. 	| Yes          	| Yes            	|


* Please note that Perfetto may not be suited for doing energy consumption measurements, see [https://github.com/S2-group/android-runner/tree/master/AndroidRunner/Plugins/perfetto#limitations-issues--caveats](here).

