
from Library import ConfigReader


class FlightBooking:


    def __init__(self, obj):
        global driver
        driver = obj


    def book_one_way_ticket(self, source, destination):
        driver.find_element_by_link_text(ConfigReader.readElements("Flight", "click_flight_loc")).click()
        driver.find_element_by_id(ConfigReader.readElements("Flight", "source_loc")).send_keys(source)
        driver.find_element_by_id(ConfigReader.readElements("Flight", "deestination_loc")).send_keys(destination)

