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

class seatingTest(unittest.TestCase):

    # Normal situation
    def testBusiness(self):
        a = AppModel()
        x = createBusiness()
        b = a.seatBusiness(x)
        self.assertEqual(0, b)





