# Import all libraries to make the application functional
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from AppModel import *
from Plane import *
from Passenger import *
import os

# -----------------------------------------------------------------------------------------------------------------

# Create all instance variables for the AppModel and the windows
app = AppModel()

managerWindow = Tk()

# All top levels are used for the multiple window structure of the app
login = Toplevel()
passengerWindow = Toplevel()
mP = Toplevel()
reportScreen = Toplevel()
categoryScreen = Toplevel()
businessTicket = Toplevel()
touristTicket = Toplevel()
familyTicket = Toplevel()

# -----------------------------------------------------------------------------------------------------------------

# Create static variables for setting up windows
mbHEIGHT = 6
mbWIDTH = 30
window = '800x800'

# Image used for the plane diagram on the manager and passenger windows
planeImage = PhotoImage(file='planelayout_New.png')

# Hard coded phrase for the manager login
managerPhrase = 'ManagerLogin'

# Variables for the checkbox used to pick categories
categories = ['Business', 'Tourist', 'Family']
# Stores the string that was chosen
clicked = StringVar()
# Sets the default category in the checkbox
clicked.set(categories[0])

# Create lists for all buttons to adjust when using the app
managerViewButtons = []
passengerViewButtons = []

# Creating more static variables for the seating method
seatX = 330
seatY = 160

# -----------------------------------------------------------------------------------------------------------------

# Setting up windows and their respective information

businessTicket.geometry(window)
businessTicket.title('Book Your Seat!')

touristTicket.geometry(window)
businessTicket.title('Book Your Seats!')

familyTicket.geometry(window)
familyTicket.title('Book Your Seats!')

categoryScreen.geometry(window)
categoryScreen.title('Choose Your Category')

passengerWindow.geometry(window)
passengerWindow.title('Guest View')

managerWindow.geometry(window)
managerWindow.title('Manager View')

mP.geometry(window)
mP.config(bg='grey')
mP.title('Manager Password')

login.geometry(window)
login.title('Login')
login.config(bg='grey')

reportScreen.geometry(window)
reportScreen.title('Passenger Report')
reportScreen.config(bg='light blue')

# -----------------------------------------------------------------------------------------------------------------

# Creating an entry box for the manager login screen that hides the phrase entered
usernameBox = Entry(mP, width=30, show='*')
usernameBox.place(relx=.4, rely=.3)

# -----------------------------------------------------------------------------------------------------------------
# Strings for the entry box labels on the ticket windows
nameLabel = "Enter Your Name:"
prefLabel = 'Enter your seat preference: \n (or enter "0" if not applicable)'

# Entry boxes for the name and preference for the business category
businessName = Entry(businessTicket, width=30)
businessName.place(relx=.4, rely=.25)
businessPref = Entry(businessTicket, width=10)
businessPref.place(relx=.45, rely=.30)

# Creating the labels for the entry boxes on the business ticket window
businessNameLabel = Label(businessTicket, text=nameLabel)
businessNameLabel.place(relx=.25, rely=.25)
businessPrefLabel = Label(businessTicket, text=prefLabel)
businessPrefLabel.place(relx=.2, rely=.28)
# -----------------------------------------------------------------------------------------------------------------

# Entry boxes for the name and preference in the tourist category window
touristName1 = Entry(touristTicket, width=30)
touristName2 = Entry(touristTicket, width=30)
touristName1.place(relx=.4, rely=.20)
touristName2.place(relx=.4, rely=.50)
touristPref1 = Entry(touristTicket, width=10)
touristPref2 = Entry(touristTicket, width=10)
touristPref1.place(relx=.4, rely=.25)
touristPref2.place(relx=.4, rely=.55)

# Labels for the name entry boxes in the tourist ticket window
touristNameLabel1 = Label(touristTicket, text=nameLabel)
touristNameLabel2 = Label(touristTicket, text=nameLabel)
touristNameLabel1.place(relx=.25, rely=.2)
touristNameLabel2.place(relx=.25, rely=.5)
# Labels for the preference entry boxes in the tourist ticket window
touristPrefLabel1 = Label(touristTicket, text=prefLabel)
touristPrefLabel2 = Label(touristTicket, text=prefLabel)
touristPrefLabel1.place(relx=.18, rely=.25)
touristPrefLabel2.place(relx=.18, rely=.55)
# -----------------------------------------------------------------------------------------------------------------

# Entry boxes for the family category window
familyName1 = Entry(familyTicket, width=30)
familyName2 = Entry(familyTicket, width=30)
familyName3 = Entry(familyTicket, width=30)
familyName4 = Entry(familyTicket, width=30)
familyName5 = Entry(familyTicket, width=30)

# Labels for the family entry boxes
familyNameLabel1 = Label(familyTicket, text=nameLabel)
familyNameLabel2 = Label(familyTicket, text=nameLabel)
familyNameLabel3 = Label(familyTicket, text=nameLabel)
familyNameLabel4 = Label(familyTicket, text=nameLabel)
familyNameLabel5 = Label(familyTicket, text=nameLabel)

# Placing all of the entry boxes and labels
familyName1.place(relx=.4, rely=.15)
familyName2.place(relx=.4, rely=.30)
familyName3.place(relx=.4, rely=.45)
familyName4.place(relx=.4, rely=.60)
familyName5.place(relx=.4, rely=.75)
familyNameLabel1.place(relx=.25, rely=.15)
familyNameLabel2.place(relx=.25, rely=.30)
familyNameLabel3.place(relx=.25, rely=.45)
familyNameLabel4.place(relx=.25, rely=.60)
familyNameLabel5.place(relx=.25, rely=.75)

# -----------------------------------------------------------------------------------------------------------------


# Defining any button functions
def bookBusinessTicket():
    """
    Method to book a business seat
    :return: None
    """
    # Creating a list for the passengers and seats to generate the tickets
    passengerList = []
    seatList = []
    # Grabs the name from the name entry box
    fullName = businessName.get()
    # Checks to see the user entered a first AND last name
    if len(fullName) > 1:
        # Splits the name into the first and last name for the passenger object
        first, last = fullName.split(' ')
        # Grabs the users preference and typecasts it into an integer for list indexing
        preference = int(businessPref.get())
        # Hides the business ticket window
        businessTicket.withdraw()
        # Clears both of the entry boxes
        businessName.delete(0, END)
        businessPref.delete(0, END)
        # Creates a new passenger object to be seated
        newPassenger = Passenger(first, last, 'Business', preference)

        # Calling the business seating algorithm from the AppModel class
        businessSeatNumber = app.seatBusiness(newPassenger)
        # Checks to see if the plane is full or not and returns a dialog box if true
        if businessSeatNumber == -1:
            messagebox.showwarning(title='Flight Overbooked', message='Sorry, this flight is currently full.')
        else:
            # Appends the passenger and seat to their lists for ticket generation
            passengerList.append(newPassenger)
            seatList.append(businessSeatNumber + 1)
            # Calls the method to generate the user's ticket
            generateTickets(passengerList, seatList)

            # Updates both views to show the newly booked seat
            passengerViewButtons[businessSeatNumber].config(bg='red')
            managerViewButtons[businessSeatNumber].config(bg='red')
            # Returns a dialog prompt letting the user know their seat
            messagebox.showinfo(title='Seat', message=f'Your seat is {businessSeatNumber + 1}')
    else:
        # Error message if the user does not enter their first and last name
        messagebox.showwarning(title='Your Name', message='Please enter your first and last name.')


def bookTouristTicket():
    """
    Method for booking the tourist's seats
    :return: None
    """
    # Creating a list for the passengers and seats to generate the tickets
    passengerList = []
    seatList = []
    # Grabs the names of both passengers
    fullName1 = touristName1.get()
    fullName2 = touristName2.get()
    # Checks to see both users entered their first and last name
    if len(fullName1) > 1 and len(fullName2) > 1:
        # Splits the names into first and last names for passenger object creation
        first1, last1 = fullName1.split(' ')
        first2, last2 = fullName2.split(' ')
        # Grabs the users preferences typecasted to integers for list indexing
        pref1 = int(touristPref1.get())
        pref2 = int(touristPref2.get())
        # Checks to see the users did not request the same seat if they enter a preference
        if (pref1 == pref2) and (pref1 != 0 and pref2 != 0):
            messagebox.showwarning(title='Seat', message='You must choose two different seats.')
        elif (pref1 > 12 and pref2 > 12) or (pref1 == 0 and pref2 == 0):
            # Hides the tourist ticket window and clears all the entry boxes in the window
            touristTicket.withdraw()
            touristName1.delete(0, END)
            touristPref1.delete(0, END)
            touristName2.delete(0, END)
            touristPref2.delete(0, END)
            # Creates two passenger objects for the tourist seating algorithm
            passenger1 = Passenger(first1, last1, 'Tourist', pref1)
            passenger2 = Passenger(first2, last2, 'Tourist', pref2)
            # Saves the two seated passengers
            touristSeat1, touristSeat2 = app.seatingAlgorithmTourist(passenger1, passenger2)
            # Checks to see if the plane is full and returns a dialog prompt if true
            if touristSeat1 == -1 or touristSeat2 == -1:
                messagebox.showwarning(title='Flight Overbooked', message='Sorry, this flight is currently full.')
            else:
                # Appends the passengers and their seats for ticket creation
                passengerList.append(passenger1)
                passengerList.append(passenger2)
                seatList.append(touristSeat1 + 1)
                seatList.append(touristSeat2 + 1)
                # Calls method to generate tickets
                generateTickets(passengerList, seatList)

                # Updates both button views for the newly seated passengers
                passengerViewButtons[touristSeat1].config(bg='red')
                passengerViewButtons[touristSeat2].config(bg='red')
                managerViewButtons[touristSeat1].config(bg='red')
                managerViewButtons[touristSeat2].config(bg='red')
                # Displays a dialog prompt with the user's seats
                messagebox.showinfo(title='Seats', message=f'Your seats are {touristSeat1 + 1} & {touristSeat2 + 1}')
        else:
            # Returns an error if the user requests business seating
            messagebox.showwarning(title='Invalid Seating', message='Seats 1-12 are reserved for Business class.')
    else:
        # Returns an error if the users do not enter their first and last names
        messagebox.showwarning(title='Your Name', message='Please enter both of your first and last names.')


def bookFamilyTicket():
    """
    Method for seating the family category
    :return: None
    """
    # Grabs the names from the entry boxes
    fullname1 = familyName1.get()
    fullname2 = familyName2.get()
    fullname3 = familyName3.get()
    fullname4 = familyName4.get()
    fullname5 = familyName5.get()
    # Checks to see if the minimum number of family members have filled in their first and last name
    if len(fullname1) > 1 and len(fullname2) > 1 and len(fullname3) > 1:
        # Creates lists for ticket generation
        passengerList = []
        seatList = []
        # Splits the full names into their first and last names
        first1, last1 = fullname1.split(' ')
        first2, last2 = fullname2.split(' ')
        first3, last3 = fullname3 .split(' ')
        # Withdraws the family ticket window and clears all the entry boxes
        familyTicket.withdraw()
        familyName1.delete(0, END)
        familyName2.delete(0, END)
        familyName3.delete(0, END)
        familyName4.delete(0, END)
        familyName5.delete(0, END)
        # Creates three passenger objects for the first three entry boxes
        passenger1 = Passenger(first1, last2, 'Family', 0)
        passenger2 = Passenger(first2, last2, 'Family', 0)
        passenger3 = Passenger(first3, last3, 'Family', 0)
        # Checks to see if a fourth family member is added
        if len(fullname4) > 1:
            # Splits the full name into the first and last name and creates a new passenger object
            first4, last4 = fullname4.split(' ')
            passenger4 = Passenger(first4, last4, 'Family', 0)
            # Checks to see if a fifth family member is added
            if len(fullname5) > 1:
                # Splits the full name into the first and last name and creates a family object
                first5, last5 = fullname5.split(' ')
                passenger5 = Passenger(first5, last5, 'Family', 0)
                # Runs the five member family algorithm for seats
                seat1, seat2, seat3, seat4, seat5 = app.familyFive(passenger1, passenger2, passenger3, passenger4, passenger5)
                # Checks to see if the plane is full and returns a prompt if true
                if seat1 == -1 or seat2 == -1 or seat3 == -1 or seat4 == -1 or seat5 == -1:
                    messagebox.showwarning(title='Flight Overbooked', message='Sorry, this flight is currently full.')
                else:
                    # Appends all five members and their seats to their lists for ticket generation
                    passengerList.append(passenger1)
                    passengerList.append(passenger2)
                    passengerList.append(passenger3)
                    passengerList.append(passenger4)
                    passengerList.append(passenger5)
                    seatList.append(seat1)
                    seatList.append(seat2)
                    seatList.append(seat3)
                    seatList.append(seat4)
                    seatList.append(seat5)
                    # Calls method for generating the tickets
                    generateTickets(passengerList, seatList)

                    # Updates each view's buttons to show the newly booked seats
                    passengerViewButtons[seat1].config(bg='red')
                    passengerViewButtons[seat2].config(bg='red')
                    passengerViewButtons[seat3].config(bg='red')
                    passengerViewButtons[seat4].config(bg='red')
                    passengerViewButtons[seat5].config(bg='red')
                    managerViewButtons[seat1].config(bg='red')
                    managerViewButtons[seat2].config(bg='red')
                    managerViewButtons[seat3].config(bg='red')
                    managerViewButtons[seat4].config(bg='red')
                    managerViewButtons[seat5].config(bg='red')
                    # Returns a dialog prompt with the family's seats
                    messagebox.showinfo(title='Seats',
                                        message=f'Your seats are {seat1 + 1}, {seat2 + 1}, {seat3 + 1}, {seat4 + 1}, & {seat5 + 1}')
            else:
                # Runs the four member algorithm
                seat3, seat2, seat1, seat4 = app.familyFour(passenger1, passenger2, passenger3, passenger4)
                # Checks to see if the plane is full and returns a error if true
                if seat1 == -1 or seat2 == -1 or seat3 == -1 or seat4 == -1:
                    messagebox.showwarning(title='Flight Overbooked', message='Sorry, this flight is currently full.')
                else:
                    # Appends all four members and their seats to their lists for ticket generation
                    passengerList.append(passenger1)
                    passengerList.append(passenger2)
                    passengerList.append(passenger3)
                    passengerList.append(passenger4)
                    seatList.append(seat1)
                    seatList.append(seat2)
                    seatList.append(seat3)
                    seatList.append(seat4)
                    # Calls method for generating tickets
                    generateTickets(passengerList, seatList)
                    # Updates the plane views to show the newly booked seats
                    passengerViewButtons[seat1].config(bg='red')
                    passengerViewButtons[seat2].config(bg='red')
                    passengerViewButtons[seat3].config(bg='red')
                    passengerViewButtons[seat4].config(bg='red')
                    managerViewButtons[seat1].config(bg='red')
                    managerViewButtons[seat2].config(bg='red')
                    managerViewButtons[seat3].config(bg='red')
                    managerViewButtons[seat4].config(bg='red')
                    # Returns dialog box with the family's seats
                    messagebox.showinfo(title='Seats',
                                        message=f'Your seats are {seat1 + 1}, {seat2 + 1}, {seat3 + 1}, & {seat4 + 1}')
        else:
            # Runs the three member algorithm
            seat3, seat2, seat1 = app.familyThree(passenger1, passenger2, passenger3)
            # Checks to see if the plane is full and returns an error if so
            if seat1 == -1 or seat2 == -1 or seat3 == -1:
                messagebox.showwarning(title='Flight Overbooked', message='Sorry, this flight is currently full.')
            else:
                # Appends the passengers and their seats to the lists for ticket generation
                passengerList.append(passenger1)
                passengerList.append(passenger2)
                passengerList.append(passenger3)
                seatList.append(seat1)
                seatList.append(seat2)
                seatList.append(seat3)
                # Calls method for generating tickets
                generateTickets(passengerList, seatList)
                # Updates plane views to show newly booked seats
                passengerViewButtons[seat1].config(bg='red')
                passengerViewButtons[seat2].config(bg='red')
                passengerViewButtons[seat3].config(bg='red')
                managerViewButtons[seat1].config(bg='red')
                managerViewButtons[seat2].config(bg='red')
                managerViewButtons[seat3].config(bg='red')
                # Returns dialog box with the family's seats
                messagebox.showinfo(title='Seats', message=f'Your seats are {seat1 + 1}, {seat2 + 1}, & {seat3 + 1}')
    else:
        # Returns an error if any of the family members do not enter their first and last name
        messagebox.showwarning(title='Your Name', message='Please enter all of your first and last names.')


def chooseCategory():
    """
    Method for the category window to choose which ticket to book
    :return: None
    """
    # Grabs which category was selected
    category = clicked.get()
    # Opens the corresponding window that was requested
    if category == 'Business':
        businessTicket.deiconify()
    elif category == 'Tourist':
        touristTicket.deiconify()
    elif category == 'Family':
        familyTicket.deiconify()
    # Hides the category selection window
    categoryScreen.withdraw()


def generateTickets(passengers: list, seats: list):
    """
    Method for generating tickets
    :param passengers: list The list of all passengers that need a generated ticket
    :param seats: list The corresponding list of all the passenger's seats
    :return: None
    """
    # Runs a loop for all of the passengers
    for i in range(len(passengers)):
        # Creates a new test file for the passenger's ticket with their seat number and last name
        ticket = open(f'_Tickets/ Seat {seats[i]:03}, {passengers[i].getLast()}', "w")
        # Writes all the necessary information into the ticket file
        ticket.write(f"Seat No. {seats[i]} \nName: {passengers[i]} \nFlight Date: 19 Apr. 2021 \nFlight: 330")
        # Closes the current ticket file
        ticket.close()


def createReport():
    """
    Method for creating the managers satisfaction report
    :return: None
    """
    # Calls the AppModel method for getting ten random passengers
    ratingList = app.generateReport()
    # String for the satisfaction report
    ratingString = ""
    # Accumulator value to total all the scores
    ratingTotal = 0
    # Loops through all passengers in the list
    for i in range(len(ratingList)):
        # Concatenates the current passengers name and their score to the master string
        ratingString += f"\n{ratingList[i]} rated {ratingList[i].getRating()}"
        # Adds the current rating to the total
        ratingTotal += ratingList[i].getRating()
    # Adds a line at the bottom showing the rating total and displays it in a dialog box
    ratingString += f"\n\nAll ratings totaled to {ratingTotal} overall!"
    messagebox.showinfo(title='Passenger Rating Report', message=f'{ratingString}')
    # Opens the flight report text file
    managerReport = open("flightReport", "w")
    # Writes the satisfaction report into the file
    managerReport.write(f'{ratingString}')
    # Closes the report file
    managerReport.close()


def quitApp():
    """
    Method for quitting out of the entire application
    :return: None
    """
    # Destroys all windows
    login.destroy()
    managerWindow.destroy()
    # Exits out of the event loop
    sys.exit()


def changeSeat():
    """
    Method for allowing a user to change their seat
    :return: None
    """
    # Dialog box asking the user to enter their name
    name = simpledialog.askstring('Name', "What is the name printed on your ticket?", parent=passengerWindow)
    # Checks to see if a name was entered
    if name is not None:
        # Splits the full name into the first and last name for verification
        first, last = name.split(" ")
        # Asks the user which seat they are sitting in
        seatNumber = int(simpledialog.askfloat('Seat', "Which seat are you currently assigned to?\n(Please enter in a numeric value)", parent=passengerWindow))
        # Checks to see if a number was entered
        if seatNumber is not None:
            # Asks the user where they'd like to move their seat to
            requestedSeat = int(simpledialog.askfloat('New Seat', "Which seat would you liked to be moved to?\n(Please enter a numeric value)", parent=passengerWindow))
            # Checks to see if a number was entered
            if requestedSeat is not None:
                # Checks to see if the requested seat is open
                if app.seatList[requestedSeat - 1].isOpen:
                    # Checks to see if the identity entered matches the passenger currently booked in that seat
                    if app.seatList[seatNumber-1].passenger.getFirst() == first and app.seatList[seatNumber-1].passenger.getLast() == last:
                        # Grabs the passenger from their previous seat
                        editPassenger = app.seatList[seatNumber - 1].passenger
                        # Checks to see if a non-business class passenger tries to sit in business
                        if editPassenger.getCat() != "Business" and requestedSeat <= 12:
                            # Error returns if true
                            messagebox.showwarning(title='Update', message='Seats 1-12 are reserved for business class only.')
                        else:
                            # Removes the passenger from their seat and sets it back to open
                            app.seatList[seatNumber - 1].removePassenger()
                            # Changes the seat on each view back to green to represent it being open
                            passengerViewButtons[seatNumber - 1].config(bg='green')
                            managerViewButtons[seatNumber - 1].config(bg='green')
                            # Checks to see if the ticket file exists
                            if os.path.exists(f"_Tickets/ Seat {seatNumber:03}, {last}"):
                                # Deletes the ticket
                                os.remove(f"_Tickets/ Seat {seatNumber:03}, {last}")

                            # Adds the passenger to their requested seat
                            app.seatList[requestedSeat - 1].addPassenger(editPassenger)
                            # Updates each view to represent the newly booked seat
                            passengerViewButtons[requestedSeat - 1].config(bg='red')
                            managerViewButtons[requestedSeat - 1].config(bg='red')
                            # Generates a new ticket for the seat change
                            generateTickets([editPassenger], [requestedSeat])
                            # Dialog box to inform the user their seat has been updated
                            messagebox.showinfo(title='Update', message='Your seat has been updated!')
                    else:
                        # Error if the name does not match the currently seated passenger
                        messagebox.showwarning(title='Update',
                                               message='The name does not match who is currently seated.')
                else:
                    # Error if the seat is currently occupied
                    messagebox.showwarning(title='Update', message='That seat is unavailable.')


def loginButton():
    """
    Method to login the manager
    :return: None
    """
    # Checks to see if the entered phrase matches the hard coded in phrase
    if usernameBox.get() == managerPhrase:
        # Opens the manager window and hides the login screen
        managerWindow.deiconify()
        mP.withdraw()
    # Clears the username box when method is called
    usernameBox.delete(0, END)


def bookSeat():
    """
    Method to open the category window
    :return: None
    """
    categoryScreen.deiconify()


def passengerLogin():
    """
    Method to open the passenger plane view
    :return: None
    """
    login.withdraw()
    passengerWindow.deiconify()


def managerLogin():
    """
    Method to open the manager login window
    :return: None
    """
    login.withdraw()
    mP.deiconify()


def logout():
    """
    Method to return to the login window from either passenger or manager view
    :return: None
    """
    login.deiconify()
    passengerWindow.withdraw()
    managerWindow.withdraw()


# -----------------------------------------------------------------------------------------------------------------

# Method for creating all 120 seat buttons for each view
def seatButtons(master, seatList, x, y):
    """
    Function to create 120 seats for the plane diagram
    :param master: str Which window the buttons are placed in
    :param seatList: list The list where all the seats are appended to
    :param x: int The starting X coordinate
    :param y: int The starting Y coordinate
    :return: None
    """
    # Loops through all 120 seats
    for i in range(1, 120 + 1):
        # Creates a new button object
        b = Button(master, text=f"{i}", bg='green', fg='white', width=2, height=1)
        # Appends the button to the button list
        seatList.append(b)
        # Places the button in specified coordinates
        b.place(x=x, y=y)
        # Shifts the next button's X coordinates over the width of a button
        x += 23
        # Checks to see if the button has hit the end of the row
        if i % 3 == 0:
            # Checks to see if the button has hit the end of the plane
            if i % 6 == 0:
                # Moves the button back to the furthest left and down to the next row
                x -= 161
                y += 25
            else:
                # Leaves a space for the walkway
                x += 23


# -----------------------------------------------------------------------------------------------------------------

# Creates the plane image and all 120 seat buttons in both windows
planeLabelPassenger = Label(passengerWindow, image=planeImage).place(x=175, y=30)
seatButtons(passengerWindow, passengerViewButtons, seatX, seatY)

planeLabelManager = Label(managerWindow, image=planeImage).place(x=175, y=30)
seatButtons(managerWindow, managerViewButtons, seatX, seatY)

# -----------------------------------------------------------------------------------------------------------------
# Creating and placing all buttons used in the GUI
bookBusiness = Button(businessTicket, text='Book', bg='blue', fg='white', command=lambda: bookBusinessTicket()).place(x=740, y=770)

bookTourist = Button(touristTicket, text='Book', bg='blue', fg='white', command=lambda: bookTouristTicket()).place(x=740, y=770)

bookFamily = Button(familyTicket, text='Book', bg='blue', fg='white', command=lambda: bookFamilyTicket()).place(x=740, y=770)

ticketButton = Button(passengerWindow, text='Book a seat', bg='blue', fg='white', command=lambda: bookSeat())
ticketButton.place(x=5, y=770)

editSeat = Button(passengerWindow, text='Change Seat', bg='blue', fg='white', command=lambda: changeSeat()).place(x=650, y=770)

categoryBox = OptionMenu(categoryScreen, clicked, *categories,)
categoryBox.place(x=350, y=300)

chooseCat = Button(categoryScreen, text='Select Category', bg='blue', fg='white', command=lambda: chooseCategory())
chooseCat.place(x=350, y=350)
# -----------------------------------------------------------------------------------------------------------------

# More button creation and placement
reportButton = Button(managerWindow, text='Print Report', bg='blue', fg='white', command=lambda: createReport()).place(x=5, y=770)

button = Button(login, text="Passenger", height=mbHEIGHT, width=mbWIDTH, command=lambda: passengerLogin()).place(relx=.363, rely=.2)

mButton = Button(login, text='Manager', height=mbHEIGHT, width=mbWIDTH, command=lambda: managerLogin()).place(relx=.363, rely=.4)

mPB = Button(mP, text="Enter", command=lambda: loginButton()).place(relx=.49, rely=.34)

quitButton = Button(login, text='Exit', height=3, width=15, command=lambda: quitApp()).place(relx=.43, rely=.87)

logoutButton = Button(managerWindow, text='Log Out', command=lambda: logout()).place(x=740, y=770)

logoutButton2 = Button(passengerWindow, text='Exit', width=6, fg='red', command=lambda: logout()).place(x=740, y=770)

# -----------------------------------------------------------------------------------------------------------------

# Withdrawing all windows we do not want to see immediately
reportScreen.withdraw()
managerWindow.withdraw()
passengerWindow.withdraw()
mP.withdraw()
categoryScreen.withdraw()
businessTicket.withdraw()
touristTicket.withdraw()
familyTicket.withdraw()

# Creating an event loop
managerWindow.mainloop()
