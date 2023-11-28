from .Browser import Browser


class FirefoxNightly(Browser):
    def __init__(self):
        # https://stackoverflow.com/a/28151563
        super(FirefoxNightly, self).__init__('org.mozilla.fenix', '.App')

