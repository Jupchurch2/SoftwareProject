class Passenger:

    def __init__(self, first: str, last: str, category: str, preference: int) -> None:
        """
        :param first: First name
        :param last: Last name
        :param category: Category (Business, Tourist, or Family)
        :param preference: Seat number which they would prefer to be seated in
        """
        self.first = first
        self.last = last
        self.category = category
        self.rating = 0
        self.preference = preference

    def getLast(self):
        """
        :return: Passenger's last name
        """
        return self.last

    def getFirst(self):
        """
        :return: Passenger's first name
        """
        return self.first

    def getCat(self):
        """
        :return: Passenger's category
        """
        return self.category
    
    def getPref(self):
        """
        :return: Seat preference for the passenger
        """
        return self.preference

    def __str__(self):
        """
        :return: Formatted first and last name of a passenger
        """
        return f"{self.first} {self.last}"

    def getRating(self):
        """
        :return: Satisfaction rating given by a passenger
        """
        return self.rating
