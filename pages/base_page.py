class BasePage:
    # base class
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://twojzegarek.eu'