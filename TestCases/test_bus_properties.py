from Base import InitiateDriver
from Pages import bus_booking

def test_booking_bus():
    driver = InitiateDriver.start_browser()
    hotel = bus_booking.BusBooking(driver)
    hotel.book_bus("Mysore", "ooty")

    InitiateDriver.close_browser()
