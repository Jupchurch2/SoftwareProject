from typing import Optional
import Passenger


class Seat:
    def __init__(self, seatNumber: int, isOpen: bool = True) -> None:
        self.isOpen = isOpen
        self.seatNumber = seatNumber
        self.passenger = None

        if self.seatNumber >= 12:
            self.businessSeat = True

    def checkPOS(self):
        return self.POS
    
    def isAvailable(self):
        return self.isOpen
    
    def addPassenger(self, Passenger):
        self.passenger = Passenger
        self.isOpen = False
        
    def checkPassengerInSeat(self):
        if self.isOpen:
            return None
        else:
            return self.passenger

    def checkNumber(self):
        return self.seatNumber


        
