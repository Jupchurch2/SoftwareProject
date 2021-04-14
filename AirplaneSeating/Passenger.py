class Passenger:
    def __init__(self, first: str, last: str, category: str, preference: int) -> None:
        self.first = first
        self.last = last
        self.category = category
        self.rating = 0
        self.preference = preference

    def getLast(self):
        return self.last

    def getFirst(self):
        return self.first

    def getCat(self):
        return self.category
    
    def getPref(self):
        return self.preference

    def __str__(self):
        return f"{self.first} {self.last}"

    def setRating(self, rating: int):
        self.rating = rating

    def getRating(self):
        return self.rating

    # Write specific method for each category