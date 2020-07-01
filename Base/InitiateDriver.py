from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import ConfigReader


def start_browser():
    global driver

    if ((ConfigReader.readConfigData("Details", "Browser")) == "chrome"):
        # path = "./Driver/chromedriver.exe"
        driver=Chrome()

    elif ((ConfigReader.readConfigData("Details", "Browser")) == "firefox"):
        path = "path of gecko driver"
        driver = Firefox(executable_path=path)
    # else:
        """Default browser when no browser is specified or some error happens """
        #path = "/navaneeth/Documents/new_chromedriver/chromedriver.exe"
        # driver = Chrome()


    driver = Chrome()
    driver.get(ConfigReader.readConfigData("Details", "Application_URL"))
    driver.fullscreen_window()

    return driver


def close_browser():
    driver.close()