import sys
import unittest

sys.path.insert(0, '..')
from AppModel import AppModel
from Plane import Seat
from Passenger import Passenger

a = 'a'
b = 'b'
c = 'c'
d = 0

def createBusiness():
    x = Passenger(a, b, c, d)
    x.category = "Business"
    return x

def createTourists():
    x, y = Passenger(a, b, c, d), Passenger(b, a, c, d)
    x.category = "Tourist"
    y.category = "Tourist"
    return x, y

def createFamily(size: int):
    if size == 3:
        a, b, c = Passenger('a', 'b', 'c', 0), Passenger('a', 'b', 'c', 0), Passenger('a', 'b', 'c', 0)
        a.category = "Family"
        b.category = "Family"
        c.category = "Family"
        return a, b, c
    elif size == 4:
        a, b, c, d = Passenger('a', 'b', 'c', 0), Passenger('a', 'b', 'c', 0), Passenger('a', 'b', 'c', 0), Passenger('a', 'b', 'c', 0)
        a.category = "Family"
        b.category = "Family"
        c.category = "Family"
        d.category = "Family"
        return a, b, c, d
    else:
        a, b, c, d, e = Passenger('a', 'b', 'c', 0), Passenger('a', 'b', 'c', 0), Passenger('a', 'b', 'c', 0), Passenger('a', 'b', 'c', 0), Passenger('a', 'b', 'c', 0)
        a.category = "Family"
        b.category = "Family"
        c.category = "Family"
        d.category = "Family"
        e.category = "Family"
        return a, b, c, d, e

class SeatingTest(unittest.TestCase):

#-----------------------------------------------------------------------------------------------------------------------

    # Empty plane; Business first passenger
    def testBusiness(self):
        a = AppModel()
        x = Passenger('a', 'b', 'Business', 0)
        b = a.seatBusiness(x)
        self.assertEqual(0, b)

    # Empty plane; Tourists first passengers
    def testTourist(self):
        a = AppModel()
        x, y = createTourists()
        b = a.seatingAlgorithmTourist(x, y)

        # Should be seated in first two non-business seats (returns 12, 13 as index into seat list; seat numbers are 13, 14)
        self.assertEqual((12, 13), b)

    # Empty plane; first 3 passengers
    def testFamilyThree(self):
        a = AppModel()
        x, y, z = createFamily(3)
        b = a.familyThree(x, y, z)

        # Should be first non-business row (index values for seat list)
        self.assertEqual((14, 13, 12), b)

    # Empty plane; first 4 passengers
    def testFamilyFour(self):
        a = AppModel()
        w, x, y, z = createFamily(4)
        b = a.familyFour(w, x, y, z)

        # Should be first non-business row (index values for seat list)
        self.assertEqual((14, 13, 12, 15), b)

    # Empty plane; first 5 passengers
    def testFamilyFive(self):
        a = AppModel()
        v, w, x, y, z = createFamily(5)
        b = a.familyFive(v, w, x, y, z)

        # Should be first non-business row (index values for seat list)
        self.assertEqual((12, 13, 14, 15, 16), b)

#-----------------------------------------------------------------------------------------------------------------------

    def testReport(self):

        # Creates over 20 passengers to be randomly chosen using the AppModel function to be sure it returns list of 10
        # Seats the passengers, since they are appended to the passenger list using the seating algorithm
        a = AppModel()
        b, c, d = createFamily(3)
        e = a.familyThree(b, c, d)
        f, g = createTourists()
        h = a.seatingAlgorithmTourist(f, g)
        i, j, k, l, m = createFamily(5)
        n = a.familyFive(i, j, k, l, m)
        o, p, q, r, s = createFamily(5)
        t = a.familyFive(o, p, q, r, s)
        u = createBusiness()
        v = a.seatBusiness(u)
        w, x = createTourists()
        y = a.seatingAlgorithmTourist(w, x)
        z, ab, ac = createFamily(3)
        ad = a.familyThree(z, ab, ac)

        # Call for generating report which should return list of 10 passenger objects and checking length
        gen = a.generateReport()
        self.assertEqual(len(gen), 10)

#-----------------------------------------------------------------------------------------------------------------------

    # Test for if business class is full
    def testFullBusiness(self):
        a = AppModel()

        # Simulates business select being full
        for seat in range(12):
            a.seatList[seat].isOpen = False

        # Checks that passenger is given the first available seat outside of business select (index = 12, seat 13)
        b = createBusiness()
        c = a.seatBusiness(b)
        self.assertEqual(12, c)

    # Ensures preference is granted
    def testBusinessPref(self):
        a = AppModel()
        b = createBusiness()
        b.preference = 110
        c = a.seatBusiness(b)
        self.assertEqual(109, c)

    # Checks full plane to make sure return value is -1 to be handled in GUI
    def testFullPlane(self):
        a = AppModel()
        for seat in range(120):
            a.seatList[seat].isOpen = False
        b = createBusiness()
        c = a.seatBusiness(b)
        self.assertEqual(-1, c)

#-----------------------------------------------------------------------------------------------------------------------

    # Ensures preference is granted
    def testTouristPref(self):
        a = AppModel()
        b, c = createTourists()
        b.preference, c.preference = 100, 103
        d = a.seatingAlgorithmTourist(b, c)
        self.assertEqual((99, 102), d)

    # Tests if the left side middle/window seats are all full
    def testTouristLeftFull(self):
        a = AppModel()
        for seat in range(12, 120, 6):
            a.seatList[seat].isOpen = False
            a.seatList[seat + 1].isOpen = False
        b, c = createTourists()
        d = a.seatingAlgorithmTourist(b, c)
        self.assertEqual((16, 17), d)

    # Tests if tourists have to be seated outside of their requirement-defined preference
    def testNoWinMidSeats(self):
        a = AppModel()
        for seat in range(12, 120, 6):
            a.seatList[seat].isOpen = False
            a.seatList[seat + 1].isOpen = False
        for seat in range(16, 120, 6):
            a.seatList[seat].isOpen = False
            a.seatList[seat + 1].isOpen = False
        b, c = createTourists()
        d = a.seatingAlgorithmTourist(b, c)
        self.assertEqual((14, 15), d)

    # Tests if the plane is full that -1 is returned to be handled in GUI
    def testTourFullPlane(self):
        a = AppModel()
        for seat in range(0, 120):
            a.seatList[seat].isOpen = False
        b, c = createTourists()
        d = a.seatingAlgorithmTourist(b, c)
        self.assertEqual((-1, -1), d)

#-----------------------------------------------------------------------------------------------------------------------

    # Tests if the left side of the plane is too full for a family of three
    def testLeftFullFamThree(self):
        a = AppModel()
        b, c, d = createFamily(3)
        for seat in range(14, 120, 6):
            a.seatList[seat].isOpen = False
        e = a.familyThree(b, c, d)
        self.assertEqual((15, 16, 17), e)

if __name__ == "__main__":
    unittest.main()

