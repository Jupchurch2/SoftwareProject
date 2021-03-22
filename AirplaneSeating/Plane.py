from typing import Optional
import Passenger


class Seat:
    def __init__(self, POS: str, seatNumber: int, isTaken: bool = False) -> None:
        self.POS = POS
        self.isTaken = isTaken
        self.seatNumber = seatNumber
        self.passenger = None
        self.businessSeat = False

        if self.seatNumber >= 12:
            self.businessSeat = True

    def checkPOS(self):
        return self.POS

    def checkSeat(self) -> Optional[Passenger]:
        if self.isTaken:
            return self.passenger
        else:
            return False

    def checkNumber(self):
        return self.seatNumber

    def isBusiness(self):
        return self.businessSeat


class Airplane:
    pass