import pathlib
"""
Setting up a chromedriver directory
Assuming the .exe file is present in the parent directory
"""

path = pathlib.Path(__file__).parent.absolute()
chromedriver = str(path) + '\chromedriver.exe'
