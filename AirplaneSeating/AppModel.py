from Plane import Seat
from Passenger import Passenger


class AppModel:
   
   def __init__(self):
      self.seatList = []
      for i in range(120):
         self.seatList[i] = Seat(i + 1, True)
      self.passengerList = []

   def seatingAlgorithmBusiness(self, passenger: Passenger):
      passengerPref = passenger.getPref() - 1
      if seatList[passengerPref].isAvailable():
         seatList[passengerPref].passenger = passenger
      
      else:
         for i in range(0, 12):
            if seatList[i].isAvailable():
               seatList[i].passenger = passenger
               # Satisfaction
               break
            elif i == 11:
               for i in range(12, 120):
                  if seatList[i].isAvailable():
                     seatList[i].passenger = passenger
                  elif i == 120:
                     raiseError("Passenger can not be seated")
                     break
               break

   def seatingAlgorithmTourist(self, passenger: Passenger, passengerTwo: Passenger):
      passengerPref = passenger.getPref() - 1
      prefTwo = passengerTwo.getPref() - 1
      availableSeatOne = -1
      availableSeatTwo = -1
      checkSeats = 0
      for i in range (12, 120):
         if seatList[i].isAvailable():
            checkSeats += 1
            if checkSeats == 1:
               availableSeatOne = i
            if checkSeats == 2:
               availableSeatTwo = i
               break
         elif i == 119:
            raiseError("Both passengers can not be seated due to spatial limitations")

      if seatList[passengerPref].isAvailable() and seatList[prefTwo].isAvailable():
         seatList[passengerPref].passenger = passenger
         seatList[prefTwo].passenger = passengerTwo
         return 0

      for i in range(12, 120, 6):
         if seatList[i].isAvailable() and seatList[i+1].isAvailable():
            seatList[i].passenger = passenger
            seatList[i+1].passenger = passengerTwo
            return 0
         else:
            for i in range(16, 120, 6):
               if seatList[i].isAvailable() and seatList[i+1].isAvailable():
                  seatList[i].passenger = passenger
                  seatList[i+1].passenger = passengerTwo
                  return 0
      for i in range(12, 120):
         if seatList[i].isAvailable() and seatList[i+1].isAvailable():
            seatList[i].passenger = passenger
            seatList[i+1].passenger = passengerTwo
            return 0

      seatList[availableSeatOne].passenger = passenger
      seatList[availableSeatTwo].passenger = passengerTwo
         



      
   
      
