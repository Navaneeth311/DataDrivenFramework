from Library import ConfigReader

class BusBooking:
    def __init__(self, obj):
        global driver
        driver = obj

    def book_bus(self, source, destination):
        driver.find_element_by_xpath(ConfigReader.readElements("Bus", "click_bus_loc"))
        driver.find_element_by_id(ConfigReader.readElements("Bus", "bus_source_loc")).send_keys(source)
        driver.find_element_by_id(ConfigReader.readElements("Bus", "bus_destination")).send_keys(destination)


