from Base import InitiateDriver
from Pages import flight_booking
from DataGeneraator import DataGen
import pytest



@pytest.mark.parametrize("data",DataGen.dataGenerator() )
def test_one_way_flight_booking(data):
    driver = InitiateDriver.start_browser()
    flights=flight_booking.FlightBooking(driver)
    flights.book_one_way_ticket(data[0], data[1])

    InitiateDriver.close_browser()

