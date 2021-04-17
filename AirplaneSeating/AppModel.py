from Plane import Seat
from Passenger import Passenger


class AppModel:

    def __init__(self):
        self.seatList = []
        for i in range(0, 120):
            self.seatList.append(Seat(i + 1, True))
        self.passengerList = []

    def seatBusiness(self, passenger: Passenger):
        passengerPref = passenger.getPref() - 1
        if self.seatList[passengerPref].isAvailable() and passengerPref != -1:
            self.seatList[passengerPref].addPassenger(passenger)
            passenger.rating = 0
            return passengerPref
        else:
            for i in range(0, 12):
                if self.seatList[i].isAvailable():
                    self.seatList[i].addPassenger(passenger)
                    passenger.rating = 0
                    return i
                elif i == 11:
                    for j in range(12, 120):
                        if self.seatList[j].isAvailable():
                            self.seatList[j].addPassenger(passenger)
                            passenger.rating = -5
                            return j
                        elif j == 120:
                            return -1



    def seatingAlgorithmTourist(self, passenger: Passenger, passengerTwo: Passenger):
        passengerPref = passenger.getPref() - 1
        prefTwo = passengerTwo.getPref() - 1
        availableSeatOne = -1
        availableSeatTwo = -1
        checkSeats = 0
        for i in range(12, 120):
            if self.seatList[i].isAvailable():
                checkSeats += 1
                if checkSeats == 1:
                    availableSeatOne = i
                if checkSeats == 2:
                    availableSeatTwo = i
                    break
            elif i == 119:
                return -1, -1

        if (self.seatList[passengerPref].isAvailable() and self.seatList[prefTwo].isAvailable()) and (
                passengerPref != -1 and prefTwo != -1):
            self.seatList[passengerPref].passenger = passenger
            self.seatList[passengerPref].isOpen = False
            self.seatList[prefTwo].passenger = passengerTwo
            self.seatList[prefTwo].isOpen = False
            passenger.rating = 10
            passengerTwo.rating = 10
            return passengerPref, prefTwo

        for i in range(12, 120, 6):
            if self.seatList[i].isAvailable() and self.seatList[i + 1].isAvailable():
                self.seatList[i].passenger = passenger
                self.seatList[i + 1].passenger = passengerTwo
                self.seatList[i].isOpen = False
                self.seatList[i + 1].isOpen = False
                passenger.rating = 15
                passengerTwo.rating = 15
                return i, i + 1

        for j in range(16, 120, 6):
            if self.seatList[j].isAvailable() and self.seatList[j + 1].isAvailable():
               self.seatList[j].passenger = passenger
               self.seatList[j + 1].passenger = passengerTwo

               self.seatList[j].isOpen = False
               self.seatList[j + 1].isOpen = False
               passenger.rating = 15
               passengerTwo.rating = 15
               return j, j + 1

        for i in range(12, 120):
            if self.seatList[i].isAvailable() and self.seatList[i + 1].isAvailable():
                self.seatList[i].passenger = passenger
                self.seatList[i + 1].passenger = passengerTwo
                self.seatList[i].isOpen = False
                self.seatList[i+1].isOpen = False
                passenger.rating = 10
                passengerTwo.rating = 10
                return i, i + 1

        self.seatList[availableSeatOne].passenger = passenger
        self.seatList[availableSeatTwo].passenger = passengerTwo

        self.seatList[availableSeatOne].isOpen = False
        self.seatList[availableSeatTwo].isOpen = False
        return availableSeatOne, availableSeatTwo

    # Needs to set open seats to false for families of 3,4 and 5
    def familyThree(self, passOne: Passenger, passTwo: Passenger, passThree: Passenger):
        availableSeatOne = -1
        availableSeatTwo = -1
        availableSeatThree = -1
        checkSeats = 0
        for i in range(12, 120):
            if self.seatList[i].isAvailable():
                checkSeats += 1
                if checkSeats == 1:
                    availableSeatOne = i
                if checkSeats == 2:
                    availableSeatTwo = i
                if checkSeats == 3:
                    availableSeatThree = i
                    break
            elif i == 119:
                return -1, -1, -1
        for i in range(14, 120, 6):
            if self.seatList[i].isAvailable() and self.seatList[i - 1].isAvailable and self.seatList[i - 2].isAvailable():
                self.seatList[i].passenger = passOne
                self.seatList[i - 1].passenger = passTwo
                self.seatList[i - 2].passenger = passThree
                self.seatList[i].isOpen = False
                self.seatList[i-1].isOpen = False
                self.seatList[i-2].isOpen = False
                passOne.rating, passTwo.rating, passThree.rating = 15, 15, 15
                return i, i - 1, i - 2
            else:
                continue
        for i in range(15, 120, 6):
            if self.seatList[i].isAvailable() and self.seatList[i+1].isAvailable and self.seatList[i+2].isAvailable():
                self.seatList[i].passenger = passOne
                self.seatList[i+1].passenger = passTwo
                self.seatList[i+2].passenger = passThree
                self.seatList[i].isOpen = False
                self.seatList[i+1].isOpen = False
                self.seatList[i+2].isOpen = False
                passOne.rating, passTwo.rating, passThree.rating = 15, 15, 15
                return i, i+1, i+2
            else:
                continue
        self.seatList[availableSeatOne].passenger = passOne
        self.seatList[availableSeatTwo].passenger = passTwo
        self.seatList[availableSeatThree].passenger = passThree
        passOne.rating, passTwo.rating, passThree.rating = -10, -10, -10
        return availableSeatOne, availableSeatTwo, availableSeatThree

    def familyFour(self, passOne: Passenger, passTwo: Passenger, passThree: Passenger, passFour: Passenger):
        availableSeatOne = -1
        availableSeatTwo = -1
        availableSeatThree = -1
        availableSeatFour = -1
        checkSeats = 0
        for i in range(12, 120):
            if self.seatList[i].isAvailable():
                checkSeats += 1
                if checkSeats == 1:
                    availableSeatOne = i
                if checkSeats == 2:
                    availableSeatTwo = i
                if checkSeats == 3:
                    availableSeatThree = i
                if checkSeats == 4:
                    availableSeatFour = i
                    break
            elif i == 119:
                return -1, -1, -1, -1
        for i in range(14, 120, 6):
            if self.seatList[i].isAvailable() and self.seatList[i - 1].isAvailable and self.seatList[
                i - 2].isAvailable():
                if i >= 20 and self.seatList[i - 6].isAvailable():
                    self.seatList[i].passenger = passOne
                    self.seatList[i - 1].passenger = passTwo
                    self.seatList[i - 2].passenger = passThree
                    self.seatList[i - 6].passenger = passFour
                    self.seatList[i].isOpen = False
                    self.seatList[i - 1].isOpen = False
                    self.seatList[i - 2].isOpen = False
                    self.seatList[i - 6].isOpen = False
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating = 15, 15, 15, 15
                    return i, i - 1, i - 2, i - 6
                elif self.seatList[i + 1].isAvailable():
                    self.seatList[i].passenger = passOne
                    self.seatList[i - 1].passenger = passTwo
                    self.seatList[i - 2].passenger = passThree
                    self.seatList[i + 1].passenger = passFour
                    self.seatList[i].isOpen = False
                    self.seatList[i-1].isOpen = False
                    self.seatList[i-2].isOpen = False
                    self.seatList[i+1].isOpen = False
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating = 15, 15, 15, 15
                    return i, i - 1, i - 2, i + 1
                elif i != 116 and self.seatList[i + 6].isAvailable():
                    self.seatList[i].passenger = passOne
                    self.seatList[i - 1].passenger = passTwo
                    self.seatList[i - 2].passenger = passThree
                    self.seatList[i + 6].passenger = passFour
                    return i, i - 1, i - 2, i + 6
                else:
                    continue
        for i in range(15, 120, 6):
            if self.seatList[i].isAvailable() and self.seatList[i + 1].isAvailable and self.seatList[
                i + 2].isAvailable():
                if i >= 21 and self.seatList[i - 6].isAvailable():
                    self.seatList[i].passenger = passOne
                    self.seatList[i + 1].passenger = passTwo
                    self.seatList[i + 2].passenger = passThree
                    self.seatList[i - 6].passenger = passFour
                    return i, i + 1, i + 2, i - 6
                elif self.seatList[i - 1].isAvailable():
                    self.seatList[i].passenger = passOne
                    self.seatList[i + 1].passenger = passTwo
                    self.seatList[i + 2].passenger = passThree
                    self.seatList[i - 1].passenger = passFour
                    return i, i + 1, i + 2, i - 1
                elif i != 117 and self.seatList[i + 6].isAvailable():
                    self.seatList[i].passenger = passOne
                    self.seatList[i + 1].passenger = passTwo
                    self.seatList[i + 2].passenger = passThree
                    self.seatList[i + 6].passenger = passFour
                    return i, i + 1, i + 2, i + 6
                else:
                    continue
        self.seatList[availableSeatOne].passenger = passOne
        self.seatList[availableSeatTwo].passenger = passTwo
        self.seatList[availableSeatThree].passenger = passThree
        self.seatList[availableSeatFour].passenger = passFour
        return availableSeatOne, availableSeatTwo, availableSeatThree, availableSeatFour

    def familyFive(self, passOne: Passenger, passTwo: Passenger, passThree: Passenger, passFour: Passenger,
                   passFive: Passenger):
        availableSeatOne = -1
        availableSeatTwo = -1
        availableSeatThree = -1
        availableSeatFour = -1
        availableSeatFive = -1
        checkSeats = 0
        for i in range(12, 120):
            if self.seatList[i].isAvailable():
                checkSeats += 1
                if checkSeats == 1:
                    availableSeatOne = i
                if checkSeats == 2:
                    availableSeatTwo = i
                if checkSeats == 3:
                    availableSeatThree = i
                if checkSeats == 4:
                    availableSeatFour = i
                if checkSeats == 5:
                    availableSeatFive = i
                    break
            elif i == 119:
                raiseError("Five passengers can not be seated due to spatial limitations.")
                return -1, -1, -1, -1, -1
        for i in range(14, 120, 6):
            if self.seatList[i - 1].isAvailable() and self.seatList[i].isAvailable() and self.seatList[i + 1].isAvailable() and self.seatList[i + 2].isAvailable():
                if self.seatList[i - 2].isAvailable():
                    self.seatList[i - 2].passenger = passOne
                    self.seatList[i - 1].passenger = passTwo
                    self.seatList[i].passenger = passThree
                    self.seatList[i + 1].passenger = passFour
                    self.seatList[i + 2].passenger = passFive
                    return i - 2, i - 1, i, i + 1, i + 2
                elif self.seatList[i + 3].isAvailable():
                    self.seatList[i + 3].passenger = passOne
                    self.seatList[i - 1].passenger = passTwo
                    self.seatList[i].passenger = passThree
                    self.seatList[i + 1].passenger = passFour
                    self.seatList[i + 2].passenger = passFive
                    return i + 3, i - 1, i, i + 1, i + 2
                else:
                    continue
        for i in range(14, 120, 6):
            if self.seatList[i - 2].isAvailable() and self.seatList[i - 1].isAvailable() and self.seatList[
                i].isAvailable():
                if i >= 20 and self.seatList[i - 6].isAvailable() and self.seatList[i - 7].isAvailable():
                    self.seatList[i - 2].passenger = passOne
                    self.seatList[i - 1].passenger = passTwo
                    self.seatList[i].passenger = passThree
                    self.seatList[i - 6].passenger = passFour
                    self.seatList[i - 7].passenger = passFive
                    return i - 2, i - 1, i, i - 6, i - 7
                elif i != 116 and self.seatList[i + 5].isAvailable() and self.seatList[i + 6].isAvailable():
                    self.seatList[i - 2].passenger = passOne
                    self.seatList[i - 1].passenger = passTwo
                    self.seatList[i].passenger = passThree
                    self.seatList[i + 5].passenger = passFour
                    self.seatList[i + 6].passenger = passFive
                    return i - 2, i - 1, i, i + 5, i + 6
                else:
                    continue
        for i in range(15, 120, 6):
            if self.seatList[i + 2].isAvailable() and self.seatList[i + 1].isAvailable() and self.seatList[
                i].isAvailable():
                if i >= 20 and self.seatList[i - 5].isAvailable() and self.seatList[i - 6].isAvailable():
                    self.seatList[i - 6].passenger = passOne
                    self.seatList[i - 5].passenger = passTwo
                    self.seatList[i].passenger = passThree
                    self.seatList[i + 1].passenger = passFour
                    self.seatList[i + 2].passenger = passFive
                    return i - 6, i - 5, i, i + 1, i + 2
                elif i != 117 and self.seatList[i + 6].isAvailable() and self.seatList[i + 7].isAvailable():
                    self.seatList[i].passenger = passOne
                    self.seatList[i + 1].passenger = passTwo
                    self.seatList[i + 2].passenger = passThree
                    self.seatList[i + 6].passenger = passFour
                    self.seatList[i + 7].passenger = passFive
                    return i, i + 1, i + 2, i + 6, i + 7
                else:
                    continue
        self.seatList[availableSeatOne].passenger = passOne
        self.seatList[availableSeatTwo].passenger = passTwo
        self.seatList[availableSeatThree].passenger = passThree
        self.seatList[availableSeatFour].passenger = passFour
        self.seatList[availableSeatFive].passenger = passFive
        return availableSeatOne, availableSeatTwo, availableSeatThree, availableSeatFour, availableSeatFive
