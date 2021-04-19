from Plane import Seat
from Passenger import Passenger
from random import *

class AppModel:

    def __init__(self):

        # Initializes a list and populates it with 120 Seat objects
        self.seatList = []
        for i in range(0, 120):
            self.seatList.append(Seat(i + 1, True))

        # Initializes another empty list to hold Passenger objects as they are created
        self.passengerList = []

    def generateReport(self):
        """
        :return: List of 10 random passengers for their satisfaction to be gauged and reported
        """
        # Initializes empty list for the Passengers objects and iteration variable
        randPassengers = []
        stopIter = 0

        # Loops through all Passenger objects and randomly chooses 1 during each iteration
        while stopIter != 10:
            randPassenger = self.passengerList[randrange(0, len(self.passengerList))]

            # Appends the random passenger to list, removes them from the Passenger list so they are not selected again
            randPassengers.append(randPassenger)
            self.passengerList.remove(randPassenger)

            # Accumulates iteration variable
            stopIter += 1
        return randPassengers

    def seatBusiness(self, passenger: Passenger):
        """
        :param passenger: Passenger object that needs a seat
        :return: Integer holding the passenger's assigned seat number
        """

        # Variable to hold passenger's preferred seat
        passengerPref = passenger.getPref() - 1

        # If the preferred seat is not occupied...
        if self.seatList[passengerPref].isAvailable() and passengerPref != -1:

            # Adds the passenger to that seat, sets rating equal to 0 since preference is granted
            self.seatList[passengerPref].addPassenger(passenger)
            passenger.rating = 0

            # Passenger appended to instance variable list for passengers
            self.passengerList.append(passenger)
            return passengerPref
        else:

            # Checks the business select seats for availability and adds the passenger to the first that is open
            for i in range(0, 12):
                if self.seatList[i].isAvailable():
                    self.seatList[i].addPassenger(passenger)
                    passenger.rating = 0
                    self.passengerList.append(passenger)
                    return i

                # If none of the business select seats are available...
                elif i == 11:

                    # Checks the rest of the seats on the plane and assigns passenger to the first available seat
                    for j in range(12, 120):
                        if self.seatList[j].isAvailable():
                            self.seatList[j].addPassenger(passenger)

                            # Sets passenger rating, then adds them to the passenger list
                            passenger.rating = -5
                            self.passengerList.append(passenger)
                            return j

                        # If no seats are available, returns -1 so that the passenger is notified that the plane is full
                        elif j == 120:
                            return -1



    def seatingAlgorithmTourist(self, passenger: Passenger, passengerTwo: Passenger):
        """
        :param passenger: First passenger to be seated
        :param passengerTwo: Second passenger to be seated
        :return: Integer value for the seat number where each passenger is seated
        """

        # Initializes preference variables
        passengerPref = passenger.getPref() - 1
        prefTwo = passengerTwo.getPref() - 1

        # Initialize variables to check for available seats
        availableSeatOne = -1
        availableSeatTwo = -1
        checkSeats = 0

        # Checks all non-business seats to make sure there are at least two available seats somewhere in the plane for
        # the tourists and stores the available seat values
        for i in range(12, 120):
            if self.seatList[i].isAvailable():
                checkSeats += 1
                if checkSeats == 1:
                    availableSeatOne = i
                if checkSeats == 2:
                    availableSeatTwo = i
                    break

            # If there are not two seats available, returns -1 default values for issue to be handled in GUI
            elif i == 119:
                return -1, -1

        # Checks to see if passenger preferences can be granted and assigns their seats if so
        if (self.seatList[passengerPref].isAvailable() and self.seatList[prefTwo].isAvailable()) and (passengerPref != -1 and prefTwo != -1):
            self.seatList[passengerPref].addPassenger(passenger)
            self.seatList[prefTwo].addPassenger(passengerTwo)

            # Sets passenger ratings and adds them to the list
            passenger.rating = 10
            passengerTwo.rating = 10
            self.passengerList.append(passenger)
            self.passengerList.append(passengerTwo)
            return passengerPref, prefTwo

        # Checks to see if window/middle seat combinations on the left side of the plane are available
        # If so, assigns passengers to those seats
        for i in range(12, 120, 6):
            if self.seatList[i].isAvailable() and self.seatList[i + 1].isAvailable():
                self.seatList[i].addPassenger(passenger)
                self.seatList[i + 1].addPassenger(passengerTwo)

                # Sets passenger ratings, adds them to the passenger list
                passenger.rating = 15
                passengerTwo.rating = 15
                self.passengerList.append(passenger)
                self.passengerList.append(passengerTwo)
                return i, i + 1

        # Checks the window/middle combinations on the right side of the plane
        # Assigns passengers to those seats if possible
        for j in range(16, 120, 6):
            if self.seatList[j].isAvailable() and self.seatList[j + 1].isAvailable():
               self.seatList[j].addPassenger(passenger)
               self.seatList[j + 1].addPassenger(passengerTwo)

               # Sets passenger ratings and adds them to passenger list
               passenger.rating = 15
               passengerTwo.rating = 15
               self.passengerList.append(passenger)
               self.passengerList.append(passengerTwo)
               return j, j + 1

        # Checks the whole plane for two side-by-side seats to keep the tourists together and assigns those seats
        # if possible
        for i in range(12, 120):
            if self.seatList[i].isAvailable() and self.seatList[i + 1].isAvailable():
                self.seatList[i].addPassenger(passenger)
                self.seatList[i + 1].addPassenger(passengerTwo)

                # Sets passenger ratings and adds them to the passenger list
                passenger.rating = 10
                passengerTwo.rating = 10
                self.passengerList.append(passenger)
                self.passengerList.append(passengerTwo)
                return i, i + 1

        # Assigns passengers to the first two available seats if no other combinations could be found
        # Sets ratings, appends them to passenger list
        self.seatList[availableSeatOne].addPassenger(passenger)
        self.seatList[availableSeatTwo].addPassenger(passengerTwo)
        self.passengerList.append(passenger)
        self.passengerList.append(passengerTwo)
        passenger.rating, passengerTwo.rating = -10, -10
        return availableSeatOne, availableSeatTwo


    def familyThree(self, passOne: Passenger, passTwo: Passenger, passThree: Passenger):
        """
        :param passOne: First passenger to be seated
        :param passTwo: Second passenger to be seated
        :param passThree: Third passenger to be seated
        :return: Integer values for seats for each passenger
        """

        # Initializes variables for checking for three available seats throughout the plane
        availableSeatOne = -1
        availableSeatTwo = -1
        availableSeatThree = -1
        checkSeats = 0

        # Loops through to check for any three open seats
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

            # If three can not be found, returns -1 default value
            elif i == 119:
                return -1, -1, -1

        # Checks for three seats grouped together to keep family together (on the left side of the plane)
        # Assigns them to those seats if possible
        for i in range(14, 120, 6):
            if self.seatList[i].isAvailable() and self.seatList[i - 1].isAvailable and self.seatList[i - 2].isAvailable():
                self.seatList[i].addPassenger(passOne)
                self.seatList[i - 1].addPassenger(passTwo)
                self.seatList[i - 2].addPassenger(passThree)

                # Sets ratings for each family member, adds them to the passenger list
                passOne.rating, passTwo.rating, passThree.rating = 15, 15, 15
                self.passengerList.append(passOne)
                self.passengerList.append(passTwo)
                self.passengerList.append(passThree)
                return i, i - 1, i - 2

        # Checks for three seats grouped together (on the right side of the plane)
        # Assigns the passengers to those three seats if possible
        for i in range(15, 120, 6):
            if self.seatList[i].isAvailable() and self.seatList[i+1].isAvailable and self.seatList[i+2].isAvailable():
                self.seatList[i].addPassenger(passOne)
                self.seatList[i+1].addPassenger(passTwo)
                self.seatList[i+2].addPassenger(passThree)

                # Sets ratings and appends passengers to the passenger list
                passOne.rating, passTwo.rating, passThree.rating = 15, 15, 15
                self.passengerList.append(passOne)
                self.passengerList.append(passTwo)
                self.passengerList.append(passThree)
                return i, i+1, i+2

        # If no three grouped seats are found, uses the first three available seats found
        self.seatList[availableSeatOne].addPassenger(passOne)
        self.seatList[availableSeatTwo].addPassenger(passTwo)
        self.seatList[availableSeatThree].addPassenger(passThree)

        # Sets ratings for each passenger and appends them to the passenger list
        passOne.rating, passTwo.rating, passThree.rating = -10, -10, -10
        self.passengerList.append(passOne)
        self.passengerList.append(passTwo)
        self.passengerList.append(passThree)
        return availableSeatOne, availableSeatTwo, availableSeatThree


    def familyFour(self, passOne: Passenger, passTwo: Passenger, passThree: Passenger, passFour: Passenger):
        """
        :param passOne: First passenger
        :param passTwo: Second passenger
        :param passThree: Third passenger
        :param passFour: Fourth passenger
        :return: Integer values for seats where passengers are seated
        """

        # Initializes variables to check plane for four available seats
        availableSeatOne = -1
        availableSeatTwo = -1
        availableSeatThree = -1
        availableSeatFour = -1
        checkSeats = 0

        # Checks plane for four available seats
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

            # If four are not found, returns -1 default values for family not to be seated
            elif i == 119:
                return -1, -1, -1, -1

        # Checks the left side of the plane for three seats plus another aisle seat in front of the other three
        # Assigns these seats if possible
        for i in range(14, 120, 6):
            if self.seatList[i].isAvailable() and self.seatList[i - 1].isAvailable and self.seatList[i - 2].isAvailable():

                # Only if i>=20 so that families are not seated in business select
                if i >= 20 and self.seatList[i - 6].isAvailable():
                    self.seatList[i].addPassenger(passOne)
                    self.seatList[i - 1].addPassenger(passTwo)
                    self.seatList[i - 2].addPassenger(passThree)
                    self.seatList[i - 6].addPassenger(passFour)

                    # Sets ratings and appends passengers to passenger list
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating = 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    return i, i - 1, i - 2, i - 6

                # Checks to see if the aisle seat across the aisle is available and uses if so
                elif self.seatList[i + 1].isAvailable():
                    self.seatList[i].addPassenger(passOne)
                    self.seatList[i - 1].addPassenger(passTwo)
                    self.seatList[i - 2].addPassenger(passThree)
                    self.seatList[i + 1].addPassenger(passFour)

                    # Sets passenger ratings and appends passengers to the list
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating = 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    return i, i - 1, i - 2, i + 1

                # If not in the last row and the seat behind those three is available, assigns passengers to those four
                elif i != 116 and self.seatList[i + 6].isAvailable():
                    self.seatList[i].addPassenger(passOne)
                    self.seatList[i - 1].addPassenger(passTwo)
                    self.seatList[i - 2].addPassenger(passThree)
                    self.seatList[i + 6].addPassenger(passFour)

                    # Sets ratings and appends passengers to the passenger list
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating = 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    return i, i - 1, i - 2, i + 6

        # Loops through to check the right side of the plane for three seats and the seat in front of those three
        # Assigns passengers to those seats if possible
        for i in range(15, 120, 6):
            if self.seatList[i].isAvailable() and self.seatList[i + 1].isAvailable and self.seatList[i + 2].isAvailable():

                # Only if i>=21 so that families are not seated in business select
                if i >= 21 and self.seatList[i - 6].isAvailable():
                    self.seatList[i].addPassenger(passOne)
                    self.seatList[i + 1].addPassenger(passTwo)
                    self.seatList[i + 2].addPassenger(passThree)
                    self.seatList[i - 6].addPassenger(passFour)

                    # Sets passenger ratings and appends passengers to the passenger list
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating = 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    return i - 6, i, i + 1, i + 2

                # Checks across the aisle
                elif self.seatList[i - 1].isAvailable():
                    self.seatList[i].addPassenger(passOne)
                    self.seatList[i + 1].addPassenger(passTwo)
                    self.seatList[i + 2].addPassenger(passThree)
                    self.seatList[i - 1].addPassenger(passFour)

                    # Sets passenger ratings and appends the passengers to the list
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating = 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    return i - 1, i, i + 1, i + 2

                # If not last row, checks for aisle seat behind original three seats found
                elif i != 117 and self.seatList[i + 6].isAvailable():
                    self.seatList[i].addPassenger(passOne)
                    self.seatList[i + 1].addPassenger(passTwo)
                    self.seatList[i + 2].addPassenger(passThree)
                    self.seatList[i + 6].addPassenger(passFour)

                    # Sets passenger ratings and appends passengers to the passenger list
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating = 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    return i, i + 1, i + 2, i + 6

        # If no other four seats are found grouped together, assigns them to the initial four open seats that were found
        # Handles ratings accordingly and appends passengers to the passenger list
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
        """
        :param passOne: First passenger
        :param passTwo: Second passenger
        :param passThree: Third passenger
        :param passFour: Fourth passenger
        :param passFive: Fifth passenger
        :return: Integer values for seats passengers are assigned to
        """

        # Initializes variables to check for any five available seats
        availableSeatOne = -1
        availableSeatTwo = -1
        availableSeatThree = -1
        availableSeatFour = -1
        availableSeatFive = -1
        checkSeats = 0

        # Loops through the plane to check for any five available seats
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

            # If five seats are not found, returns -1 default values so that family is not seated
            elif i == 119:
                return -1, -1, -1, -1, -1

        # Checks the left side of the plane for five seats grouped together with two aisle seats
        # Assigns those seats if possible
        for i in range(14, 120, 6):
            if self.seatList[i - 1].isAvailable() and self.seatList[i].isAvailable() and self.seatList[i + 1].isAvailable() and self.seatList[i + 2].isAvailable():

                # If the left window seat is available, assigns that and four seats to the right
                if self.seatList[i - 2].isAvailable():
                    self.seatList[i - 2].addPassenger(passOne)
                    self.seatList[i - 1].addPassenger(passTwo)
                    self.seatList[i].addPassenger(passThree)
                    self.seatList[i + 1].addPassenger(passFour)
                    self.seatList[i + 2].addPassenger(passFive)

                    # Sets ratings for passengers and appends passengers to the passenger list
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating, passFive.rating = 15, 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    self.passengerList.append(passFive)
                    return i - 2, i - 1, i, i + 1, i + 2

                # If the right window seat is available, assigns that seat and the four seats to the left
                elif self.seatList[i + 3].isAvailable():
                    self.seatList[i + 3].addPassenger(passOne)
                    self.seatList[i - 1].addPassenger(passTwo)
                    self.seatList[i].addPassenger(passThree)
                    self.seatList[i + 1].addPassenger(passFour)
                    self.seatList[i + 2].addPassenger(passFive)

                    # Sets passenger ratings and appends passengers to the passenger list
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating, passFive.rating = 15, 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    self.passengerList.append(passFive)
                    return i + 3, i - 1, i, i + 1, i + 2

        # Checks three consecutive seats on the left side
        for i in range(14, 120, 6):
            if self.seatList[i - 2].isAvailable() and self.seatList[i - 1].isAvailable() and self.seatList[i].isAvailable():

                # If the middle and aisle seats in front are also available, assigns those five
                if i >= 20 and self.seatList[i - 6].isAvailable() and self.seatList[i - 7].isAvailable():
                    self.seatList[i - 2].addPassenger(passOne)
                    self.seatList[i - 1].addPassenger(passTwo)
                    self.seatList[i].addPassenger(passThree)
                    self.seatList[i - 6].addPassenger(passFour)
                    self.seatList[i - 7].addPassenger(passFive)

                    # Sets passenger ratings and appends passengers to the passenger list
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating, passFive.rating = 15, 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    self.passengerList.append(passFive)
                    return i - 2, i - 1, i, i - 6, i - 7

                # If not the last row, checks for the middle and aisle seats behind and assigns if possible
                elif i != 116 and self.seatList[i + 5].isAvailable() and self.seatList[i + 6].isAvailable():
                    self.seatList[i - 2].addPassenger(passOne)
                    self.seatList[i - 1].addPassenger(passTwo)
                    self.seatList[i].addPassenger(passThree)
                    self.seatList[i + 5].addPassenger(passFour)
                    self.seatList[i + 6].addPassenger(passFive)

                    # Sets passenger ratings and appends passengers to the passenger list
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating, passFive.rating = 15, 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    self.passengerList.append(passFive)
                    return i - 2, i - 1, i, i + 5, i + 6

        # Checks the for three seats on the right side of the plane
        for i in range(15, 120, 6):
            if self.seatList[i + 2].isAvailable() and self.seatList[i + 1].isAvailable() and self.seatList[i].isAvailable():

                # If the middle and aisle seats in front are available, assigns passengers to those five seats
                if i >= 20 and self.seatList[i - 5].isAvailable() and self.seatList[i - 6].isAvailable():
                    self.seatList[i - 6].addPassenger(passOne)
                    self.seatList[i - 5].addPassenger(passTwo)
                    self.seatList[i].addPassenger(passThree)
                    self.seatList[i + 1].addPassenger(passFour)
                    self.seatList[i + 2].addPassenger(passFive)

                    # Sets passenger ratings and appends passengers to the passenger list
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating, passFive.rating = 15, 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    self.passengerList.append(passFive)
                    return i - 6, i - 5, i, i + 1, i + 2

                # If not last row, checks the middle and aisle seats behind and assigns if possible
                elif i != 117 and self.seatList[i + 6].isAvailable() and self.seatList[i + 7].isAvailable():
                    self.seatList[i].addPassenger(passOne)
                    self.seatList[i + 1].addPassenger(passTwo)
                    self.seatList[i + 2].addPassenger(passThree)
                    self.seatList[i + 6].addPassenger(passFour)
                    self.seatList[i + 7].addPassenger(passFive)

                    # Sets passenger ratings and appends passengers to the passenger list
                    passOne.rating, passTwo.rating, passThree.rating, passFour.rating, passFive.rating = 15, 15, 15, 15, 15
                    self.passengerList.append(passOne)
                    self.passengerList.append(passTwo)
                    self.passengerList.append(passThree)
                    self.passengerList.append(passFour)
                    self.passengerList.append(passFive)
                    return i, i + 1, i + 2, i + 6, i + 7

        # If no other conditions could were met, assigns the first five available seats previously found in the plane
        self.seatList[availableSeatOne].addPassenger(passOne)
        self.seatList[availableSeatTwo].addPassenger(passTwo)
        self.seatList[availableSeatThree].addPassenger(passThree)
        self.seatList[availableSeatFour].addPassenger(passFour)
        self.seatList[availableSeatFive].addPassenger(passFive)

        # Sets passenger ratings accordingly and appends the passengers to the list
        passOne.rating, passTwo.rating, passThree.rating, passFour.rating, passFive.rating = -10, -10, -10, -10, -10
        self.passengerList.append(passOne)
        self.passengerList.append(passTwo)
        self.passengerList.append(passThree)
        self.passengerList.append(passFour)
        self.passengerList.append(passFive)
        return availableSeatOne, availableSeatTwo, availableSeatThree, availableSeatFour, availableSeatFive
