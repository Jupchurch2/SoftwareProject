from typing import Optional
import Passenger


class Seat:
    def __init__(self, POS: str, seatNumber: int, isOpen: bool = True) -> None:
        self.POS = POS
        self.isOpen = isOpen
        self.seatNumber = seatNumber
        self.passenger = None
        self.businessSeat = False

        if self.seatNumber >= 12:
            self.businessSeat = True

    def checkPOS(self):
        return self.POS

    def checkSeat(self) -> Optional[Passenger]:
        if self.isOpen:
            return None
        else:
            return self.passenger

    def checkNumber(self):
        return self.seatNumber

    def isBusiness(self):
        return self.businessSeat


# class Airplane:
    
    # def __init__(self, passengerList: list, seatList: list)
        # self.passengerList
    
    # def seatingAlgorithm(self, Passenger):
        
