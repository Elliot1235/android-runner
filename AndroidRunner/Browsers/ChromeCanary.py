from .Browser import Browser


class ChromeCanary(Browser):
    def __init__(self):
        # https://stackoverflow.com/a/28151563
        super(ChromeCanary, self).__init__('com.chrome.canary', 'com.google.android.apps.chrome.Main')

