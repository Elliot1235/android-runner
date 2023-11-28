from .Browsers import Chrome, Firefox, Opera,ChromeCanary, FirefoxNightly


class BrowserFactory(object):
    @staticmethod
    def get_browser(name):
        if name == "chrome":
            return Chrome.Chrome
        if name == "firefox":
            return Firefox.Firefox
        if name == "ChromeCanary":
            return ChromeCanary.ChromeCanary
        if name == "FirefoxNightly":
            return FirefoxNightly.FirefoxNightly
	#if name == "opera":
            #return Opera.Opera
        raise Exception("No Browser found")
