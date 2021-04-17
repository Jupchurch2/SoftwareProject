from Plane import Seat
from Passenger import Passenger


class AppModel:

    def __init__(self):
        self.seatList = []
        for i in range(0, 120):
            self.seatList.append(Seat(i + 1, True))
        self.passengerList = []

    def generateReport(self):
        randPassengers = []
        stopIter = 0
        for i in rand(range(0, len(self.passengerList))):
            randPassengers.append(self.passengerList[i])
            stopIter += 1
            if stopIter == 10:
                break
        return randPassengers

    def seatBusiness(self, passenger: Passenger):
        passengerPref = passenger.getPref() - 1
        if self.seatList[passengerPref].isAvailable() and passengerPref != -1:
            self.seatList[passengerPref].addPassenger(passenger)
            passenger.rating = 0
            self.passengerList.append(passenger)
            return passengerPref
        else:
            for i in range(0, 12):
                if self.seatList[i].isAvailable():
                    self.seatList[i].addPassenger(passenger)
                    passenger.rating = 0
                    self.passengerList.append(passenger)
                    return i
                elif i == 11:
                    for j in range(12, 120):
                        if self.seatList[j].isAvailable():
                            self.seatList[j].addPassenger(passenger)
                            passenger.rating = -5
                            self.passengerList.append(passenger)
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

        if (self.seatList[passengerPref].isAvailable() and self.seatList[prefTwo].isAvailable()) and (passengerPref != -1 and prefTwo != -1):
            self.seatList[passengerPref].addPassenger(passenger)
            self.seatList[prefTwo].addPassenger(passengerTwo)
            passenger.rating = 10
            passengerTwo.rating = 10
            self.passengerList.append(passenger)
            self.passengerList.append(passengerTwo)
            return passengerPref, prefTwo

        for i in range(12, 120, 6):
            if self.seatList[i].isAvailable() and self.seatList[i + 1].isAvailable():
                self.seatList[i].addPassenger(passenger)
                self.seatList[i + 1].addPassenger(passengerTwo)
                passenger.rating = 15
                passengerTwo.rating = 15
                self.passengerList.append(passenger)
                self.passengerList.append(passengerTwo)
                return i, i + 1

        for j in range(16, 120, 6):
            if self.seatList[j].isAvailable() and self.seatList[j + 1].isAvailable():
               self.seatList[j].addPassenger(passenger)
               self.seatList[j + 1].addPassenger(passengerTwo)
               passenger.rating = 15
               passengerTwo.rating = 15
               self.passengerList.append(passenger)
               self.passengerList.append(passengerTwo)
               return j, j + 1

        for i in range(12, 120):
            if self.seatList[i].isAvailable() and self.seatList[i + 1].isAvailable():
                self.seatList[i].addPassenger(passenger)
                self.seatList[i + 1].addPassenger(passengerTwo)
                passenger.rating = 10
                passengerTwo.rating = 10
                self.passengerList.append(passenger)
                self.passengerList.append(passengerTwo)
                return i, i + 1

        self.seatList[availableSeatOne].addPassenger(passenger)
        self.seatList[availableSeatTwo].addPassenger(passengerTwo)
        self.passengerList.append(passenger)
        self.passengerList.append(passengerTwo)
        passenger.rating, passengerTwo.rating = -10, -10
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
                self.seatList[i].addPassenger(passOne)
                self.seatList[i - 1].addPassenger(passTwo)
                self.seatList[i - 2].addPassenger(passThree)
                passOne.rating, passTwo.rating, passThree.rating = 15, 15, 15
                self.passengerList.append(passOne)
                self.passengerList.append(passTwo)
                self.passengerList.append(passThree)
                return i, i - 1, i - 2
        for i in range(15, 120, 6):
            if self.seatList[i].isAvailable() and self.seatList[i+1].isAvailable and self.seatList[i+2].isAvailable():
                self.seatList[i].addPassenger(passOne)
                self.seatList[i+1].addPassenger(passTwo)
                self.seatList[i+2].addPassenger(passThree)
                passOne.rating, passTwo.rating, passThree.rating = 15, 15, 15
                self.passengerList.append(passOne)
                self.passengerList.append(passTwo)
                self.passengerList.append(passThree)
                return i, i+1, i+2
        self.seatList[availableSeatOne].addPassenger(passOne)
        self.seatList[availableSeatTwo].addPassenger(passTwo)
        self.seatList[availableSeatThree].addPassenger(passThree)
        passOne.rating, passTwo.rating, passThree.rating = -10, -10, -10
        self.passengerList.append(passOne)
        self.passengerList.append(passTwo)
        self.passengerList.append(passThree)
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
            if self.seatList[i].isAvailable() and self.seatList[i - 1].isAvailable and self.seatList[i - 2].isAvailable():
                if i >= 20 and self.seatList[i - 6].isAvailable():
                    self.seatList[i].addPassenger(passOne)
                    self.seatList[i - 1].addPassenger(passTwo)
                    self.seatList[i - 2].addPassenger(passThree)
                    self.seatList[i - 6].addPassenger(passFour)
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating = 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    return i, i - 1, i - 2, i - 6
                elif self.seatList[i + 1].isAvailable():
                    self.seatList[i].addPassenger(passOne)
                    self.seatList[i - 1].addPassenger(passTwo)
                    self.seatList[i - 2].addPassenger(passThree)
                    self.seatList[i + 1].addPassenger(passFour)
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating = 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    return i, i - 1, i - 2, i + 1
                elif i != 116 and self.seatList[i + 6].isAvailable():
                    self.seatList[i].addPassenger(passOne)
                    self.seatList[i - 1].addPassenger(passTwo)
                    self.seatList[i - 2].addPassenger(passThree)
                    self.seatList[i + 6].addPassenger(passFour)
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating = 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    return i, i - 1, i - 2, i + 6
        for i in range(15, 120, 6):
            if self.seatList[i].isAvailable() and self.seatList[i + 1].isAvailable and self.seatList[i + 2].isAvailable():
                if i >= 21 and self.seatList[i - 6].isAvailable():
                    self.seatList[i].addPassenger(passOne)
                    self.seatList[i + 1].addPassenger(passTwo)
                    self.seatList[i + 2].addPassenger(passThree)
                    self.seatList[i - 6].addPassenger(passFour)
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating = 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    return i, i + 1, i + 2, i - 6
                elif self.seatList[i - 1].isAvailable():
                    self.seatList[i].addPassenger(passOne)
                    self.seatList[i + 1].addPassenger(passTwo)
                    self.seatList[i + 2].addPassenger(passThree)
                    self.seatList[i - 1].addPassenger(passFour)
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating = 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    return i, i + 1, i + 2, i - 1
                elif i != 117 and self.seatList[i + 6].isAvailable():
                    self.seatList[i].addPassenger(passOne)
                    self.seatList[i + 1].addPassenger(passTwo)
                    self.seatList[i + 2].addPassenger(passThree)
                    self.seatList[i + 6].addPassenger(passFour)
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating = 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    return i, i + 1, i + 2, i + 6
        self.seatList[availableSeatOne].addPassenger(passOne)
        self.seatList[availableSeatTwo].addPassenger(passTwo)
        self.seatList[availableSeatThree].addPassenger(passThree)
        self.seatList[availableSeatFour].addPassenger(passFour)
        passOne.rating, passTwo.rating, passThree.rating, passFour.rating = -10, -10, -10, -10
        self.passengerList.append(passOne)
        self.passengerList.append(passTwo)
        self.passengerList.append(passThree)
        self.passengerList.append(passFour)
        return availableSeatOne, availableSeatTwo, availableSeatThree, availableSeatFour

    def familyFive(self, passOne: Passenger, passTwo: Passenger, passThree: Passenger, passFour: Passenger,passFive: Passenger):
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
                return -1, -1, -1, -1, -1
        for i in range(14, 120, 6):
            if self.seatList[i - 1].isAvailable() and self.seatList[i].isAvailable() and self.seatList[i + 1].isAvailable() and self.seatList[i + 2].isAvailable():
                if self.seatList[i - 2].isAvailable():
                    self.seatList[i - 2].addPassenger(passOne)
                    self.seatList[i - 1].addPassenger(passTwo)
                    self.seatList[i].addPassenger(passThree)
                    self.seatList[i + 1].addPassenger(passFour)
                    self.seatList[i + 2].addPassenger(passFive)
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating, passFive.rating = 15, 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    self.passengerList.append(passFive)
                    return i - 2, i - 1, i, i + 1, i + 2
                elif self.seatList[i + 3].isAvailable():
                    self.seatList[i + 3].addPassenger(passOne)
                    self.seatList[i - 1].addPassenger(passTwo)
                    self.seatList[i].addPassenger(passThree)
                    self.seatList[i + 1].addPassenger(passFour)
                    self.seatList[i + 2].addPassenger(passFive)
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating, passFive.rating = 15, 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    self.passengerList.append(passFive)
                    return i + 3, i - 1, i, i + 1, i + 2
        for i in range(14, 120, 6):
            if self.seatList[i - 2].isAvailable() and self.seatList[i - 1].isAvailable() and self.seatList[i].isAvailable():
                if i >= 20 and self.seatList[i - 6].isAvailable() and self.seatList[i - 7].isAvailable():
                    self.seatList[i - 2].addPassenger(passOne)
                    self.seatList[i - 1].addPassenger(passTwo)
                    self.seatList[i].addPassenger(passThree)
                    self.seatList[i - 6].addPassenger(passFour)
                    self.seatList[i - 7].addPassenger(passFive)
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating, passFive.rating = 15, 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    self.passengerList.append(passFive)
                    return i - 2, i - 1, i, i - 6, i - 7
                elif i != 116 and self.seatList[i + 5].isAvailable() and self.seatList[i + 6].isAvailable():
                    self.seatList[i - 2].addPassenger(passOne)
                    self.seatList[i - 1].addPassenger(passTwo)
                    self.seatList[i].addPassenger(passThree)
                    self.seatList[i + 5].addPassenger(passFour)
                    self.seatList[i + 6].addPassenger(passFive)
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating, passFive.rating = 15, 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    self.passengerList.append(passFive)
                    return i - 2, i - 1, i, i + 5, i + 6
        for i in range(15, 120, 6):
            if self.seatList[i + 2].isAvailable() and self.seatList[i + 1].isAvailable() and self.seatList[i].isAvailable():
                if i >= 20 and self.seatList[i - 5].isAvailable() and self.seatList[i - 6].isAvailable():
                    self.seatList[i - 6].addPassenger(passOne)
                    self.seatList[i - 5].addPassenger(passTwo)
                    self.seatList[i].addPassenger(passThree)
                    self.seatList[i + 1].addPassenger(passFour)
                    self.seatList[i + 2].addPassenger(passFive)
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating, passFive.rating = 15, 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    self.passengerList.append(passFive)
                    return i - 6, i - 5, i, i + 1, i + 2
                elif i != 117 and self.seatList[i + 6].isAvailable() and self.seatList[i + 7].isAvailable():
                    self.seatList[i].addPassenger(passOne)
                    self.seatList[i + 1].addPassenger(passTwo)
                    self.seatList[i + 2].addPassenger(passThree)
                    self.seatList[i + 6].addPassenger(passFour)
                    self.seatList[i + 7].addPassenger(passFive)
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating, passFive.rating = 15, 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    self.passengerList.append(passFive)
                    return i, i + 1, i + 2, i + 6, i + 7
        self.seatList[availableSeatOne].addPassenger(passOne)
        self.seatList[availableSeatTwo].addPassenger(passTwo)
        self.seatList[availableSeatThree].addPassenger(passThree)
        self.seatList[availableSeatFour].addPassenger(passFour)
        self.seatList[availableSeatFive].addPassenger(passFive)
        passOne.rating, passTwo.rating, passThree.rating, passFour.rating, passFive.rating = -10, -10, -10, -10, -10
        self.passengerList.append(passOne)
        self.passengerList.append(passTwo)
        self.passengerList.append(passThree)
        self.passengerList.append(passFour)
        self.passengerList.append(passFive)
        return availableSeatOne, availableSeatTwo, availableSeatThree, availableSeatFour, availableSeatFive
