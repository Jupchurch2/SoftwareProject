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
        a, b, c = 3 * Passenger('a', 'b', 'c', 0)
        a.category = "Family"
        b.category = "Family"
        c.category = "Family"
        return a, b, c
    elif size == 4:
        a, b, c, d = 4 * Passenger('a', 'b', 'c', 0)
        a.category = "Family"
        b.category = "Family"
        c.category = "Family"
        d.category = "Family"
        return a, b, c, d
    else:
        a, b, c, d, e = 5 * Passenger('a', 'b', 'c', 0)
        a.category = "Family"
        b.category = "Family"
        c.category = "Family"
        d.category = "Family"
        e.category = "Family"
        return a, b, c, d, e

class SeatingTest(unittest.TestCase):

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

    def testFamilyThree(self):



if __name__ == "__main__":
    unittest.main()

