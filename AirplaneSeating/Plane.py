from typing import Optional
import Passenger

class Seat:

    def __init__(self, seatNumber: int, isOpen: bool = True) -> None:
        """
        :param seatNumber: Seat number to be associated with the object
        :param isOpen: Availability status
        """
        self.isOpen = isOpen
        self.seatNumber = seatNumber
        self.passenger = None

        # Adds an optional instance variable regarding whether or not the seat is Business Select
        if self.seatNumber <= 12:
            self.businessSeat = True
    
    def isAvailable(self):
        """
        :return: Boolean valued instance variable regarding availability of a seat
        """
        return self.isOpen
    
    def addPassenger(self, Passenger):
        """
        :param Passenger: Takes a Passenger object to be able to tie that passenger to a seat object
        :return: None
        """
        # Sets seat passenger to be the Passenger object passed as a parameter
        # Sets the seat availability to false so seats are not double booked
        self.passenger = Passenger
        self.isOpen = False

    def removePassenger(self):
        """
        :return: None
        """
        # Reverses the actions of addPassenger by opening up a seat
        self.passenger = None
        self.isOpen = True

