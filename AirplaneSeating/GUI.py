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
planeImage = PhotoImage(file='planelayout_New.png')
managerPhrase = 'ManagerLogin'
categories = ['Business', 'Tourist', 'Family']
clicked = StringVar()
clicked.set(categories[0])

# Create lists for all buttons to adjust when using the app
managerViewButtons = []
passengerViewButtons = []

# Creating more static variables
seatX = 330
seatY = 160

# -----------------------------------------------------------------------------------------------------------------

# Setting up window information

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

# Creating entry boxes and any menus for certain windows
usernameBox = Entry(mP, width=30, show='*')
usernameBox.place(relx=.4, rely=.3)

categoryBox = OptionMenu(categoryScreen, clicked, *categories,)
categoryBox.place(relx=.4, rely=.3)

# -----------------------------------------------------------------------------------------------------------------
nameLabel = "Enter Your Name:"
prefLabel = 'Enter your seat preference: \n (or enter "0" if not applicable)'

businessName = Entry(businessTicket, width=30)
businessName.place(relx=.4, rely=.25)

businessNameLabel = Label(businessTicket, text=nameLabel)
businessNameLabel.place(relx=.25, rely=.25)

businessPref = Entry(businessTicket, width=10)
businessPref.place(relx=.45, rely=.30)

businessPrefLabel = Label(businessTicket, text=prefLabel)
businessPrefLabel.place(relx=.2, rely=.28)
# -----------------------------------------------------------------------------------------------------------------

touristName1 = Entry(touristTicket, width=30)
touristName2 = Entry(touristTicket, width=30)
touristName1.place(relx=.4, rely=.20)
touristName2.place(relx=.4, rely=.50)

touristNameLabel1 = Label(touristTicket, text=nameLabel)
touristNameLabel2 = Label(touristTicket, text=nameLabel)
touristNameLabel1.place(relx=.25, rely=.2)
touristNameLabel2.place(relx=.25, rely=.5)

touristPref1 = Entry(touristTicket, width=10)
touristPref2 = Entry(touristTicket, width=10)
touristPref1.place(relx=.4, rely=.25)
touristPref2.place(relx=.4, rely=.55)

touristPrefLabel1 = Label(touristTicket, text=prefLabel)
touristPrefLabel2 = Label(touristTicket, text=prefLabel)
touristPrefLabel1.place(relx=.18, rely=.25)
touristPrefLabel2.place(relx=.18, rely=.55)
# -----------------------------------------------------------------------------------------------------------------

familyName1 = Entry(familyTicket, width=30)
familyName2 = Entry(familyTicket, width=30)
familyName3 = Entry(familyTicket, width=30)
familyName4 = Entry(familyTicket, width=30)
familyName5 = Entry(familyTicket, width=30)

familyNameLabel1 = Label(familyTicket, text=nameLabel)
familyNameLabel2 = Label(familyTicket, text=nameLabel)
familyNameLabel3 = Label(familyTicket, text=nameLabel)
familyNameLabel4 = Label(familyTicket, text=nameLabel)
familyNameLabel5 = Label(familyTicket, text=nameLabel)

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


# Defining button functions
def bookBusinessTicket():
    passengerList = []
    seatList = []
    fullName = businessName.get()
    if len(fullName) > 1:
        first, last = fullName.split(' ')
        preference = int(businessPref.get())
        businessTicket.withdraw()
        newPassenger = Passenger(first, last, 'Business', preference)

        businessSeatNumber = app.seatBusiness(newPassenger)
        if businessSeatNumber == -1:
            messagebox.showwarning(title='Flight Overbooked', message='Sorry, this flight is currently full.')
        else:
            passengerList.append(newPassenger)
            seatList.append(businessSeatNumber + 1)
            generateTickets(passengerList, seatList)

            passengerViewButtons[businessSeatNumber].config(bg='red')
            managerViewButtons[businessSeatNumber].config(bg='red')
            messagebox.showinfo(title='Seat', message=f'Your seat is {businessSeatNumber + 1}')
    else:
        messagebox.showwarning(title='Your Name', message='Please enter your first and last name.')


def bookTouristTicket():
    passengerList = []
    seatList = []
    fullName1 = touristName1.get()
    fullName2 = touristName2.get()
    if len(fullName1) > 1 and len(fullName2) > 1:
        first1, last1 = fullName1.split(' ')
        first2, last2 = fullName2.split(' ')
        pref1 = int(touristPref1.get())
        pref2 = int(touristPref2.get())
        if (pref1 == pref2) and (pref1 != 0 and pref2 != 0):
            messagebox.showwarning(title='Seat', message='You must choose two different seats.')
        elif (pref1 > 12 and pref2 > 12) or (pref1 == 0 and pref2 == 0):
            touristTicket.withdraw()
            passenger1 = Passenger(first1, last1, 'Tourist', pref1)
            passenger2 = Passenger(first2, last2, 'Tourist', pref2)

            touristSeat1, touristSeat2 = app.seatingAlgorithmTourist(passenger1, passenger2)
            if touristSeat1 == -1 or touristSeat2 == -1:
                messagebox.showwarning(title='Flight Overbooked', message='Sorry, this flight is currently full.')
            else:
                passengerList.append(passenger1)
                passengerList.append(passenger2)
                seatList.append(touristSeat1 + 1)
                seatList.append(touristSeat2 + 1)
                generateTickets(passengerList, seatList)

                passengerViewButtons[touristSeat1].config(bg='red')
                passengerViewButtons[touristSeat2].config(bg='red')
                managerViewButtons[touristSeat1].config(bg='red')
                managerViewButtons[touristSeat2].config(bg='red')

            messagebox.showinfo(title='Seats', message=f'Your seats are {touristSeat1 + 1} & {touristSeat2 + 1}')
        else:
            messagebox.showwarning(title='Invalid Seating', message='Seats 1-12 are reserved for Business class.')
    else:
        messagebox.showwarning(title='Your Name', message='Please enter both of your first and last names.')


def bookFamilyTicket():
    fullname1 = familyName1.get()
    fullname2 = familyName2.get()
    fullname3 = familyName3.get()
    fullname4 = familyName4.get()
    fullname5 = familyName5.get()

    if len(fullname1) > 1 and len(fullname2) > 1 and len(fullname3) > 1:
        passengerList = []
        seatList = []
        first1, last1 = fullname1.split(' ')
        first2, last2 = fullname2.split(' ')
        first3, last3 = fullname3 .split(' ')
        familyTicket.withdraw()
        passenger1 = Passenger(first1, last2, 'Family', 0)
        passenger2 = Passenger(first2, last2, 'Family', 0)
        passenger3 = Passenger(first3, last3, 'Family', 0)
        if len(fullname4) > 1:
            first4, last4 = fullname4.split(' ')
            passenger4 = Passenger(first4, last4, 'Family', 0)
            if len(fullname5) > 1:
                first5, last5 = fullname5.split(' ')
                passenger5 = Passenger(first5, last5, 'Family', 0)

                seat1, seat2, seat3, seat4, seat5 = app.familyFive(passenger1, passenger2, passenger3, passenger4, passenger5)
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
                generateTickets(passengerList, seatList)

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

                messagebox.showinfo(title='Seats',
                                    message=f'Your seats are {seat1 + 1}, {seat2 + 1}, {seat3 + 1}, {seat4 + 1}, & {seat5 + 1}')
            else:
                seat3, seat2, seat1, seat4 = app.familyFour(passenger1, passenger2, passenger3, passenger4)
                passengerList.append(passenger1)
                passengerList.append(passenger2)
                passengerList.append(passenger3)
                passengerList.append(passenger4)
                seatList.append(seat1)
                seatList.append(seat2)
                seatList.append(seat3)
                seatList.append(seat4)
                generateTickets(passengerList, seatList)

                passengerViewButtons[seat1].config(bg='red')
                passengerViewButtons[seat2].config(bg='red')
                passengerViewButtons[seat3].config(bg='red')
                passengerViewButtons[seat4].config(bg='red')
                managerViewButtons[seat1].config(bg='red')
                managerViewButtons[seat2].config(bg='red')
                managerViewButtons[seat3].config(bg='red')
                managerViewButtons[seat4].config(bg='red')

                messagebox.showinfo(title='Seats', message=f'Your seats are {seat1 + 1}, {seat2 + 1}, {seat3 + 1}, & {seat4 + 1}')
        else:
            seat3, seat2, seat1 = app.familyThree(passenger1, passenger2, passenger3)

            passengerList.append(passenger1)
            passengerList.append(passenger2)
            passengerList.append(passenger3)
            seatList.append(seat1)
            seatList.append(seat2)
            seatList.append(seat3)
            generateTickets(passengerList, seatList)

            passengerViewButtons[seat1].config(bg='red')
            passengerViewButtons[seat2].config(bg='red')
            passengerViewButtons[seat3].config(bg='red')
            managerViewButtons[seat1].config(bg='red')
            managerViewButtons[seat2].config(bg='red')
            managerViewButtons[seat3].config(bg='red')

            messagebox.showinfo(title='Seats', message=f'Your seats are {seat1 + 1}, {seat2 + 1}, & {seat3 + 1}')

    else:
        messagebox.showwarning(title='Your Name', message='Please enter all of your first and last names.')

def chooseCategory():
    category = clicked.get()
    if category == 'Business':
        businessTicket.deiconify()
    elif category == 'Tourist':
        touristTicket.deiconify()
    elif category == 'Family':
        familyTicket.deiconify()
    categoryScreen.withdraw()

def generateTickets(passengers: list, seats: list):
    for i in range(len(passengers)):
        ticket = open(f'_Tickets/ Seat {seats[i]:03}, {passengers[i].getLast()}', "w")
        ticket.write(f"Seat No. {seats[i]} \nName: {passengers[i]} \nFlight Date: 19 Apr. 2021 \nFlight: 330")
        ticket.close()

def createReport():
    ratingList = app.generateReport()
    ratingString = ""
    ratingTotal = 0
    for i in range(len(ratingList)):
        ratingString += f"\n{ratingList[i]} rated {ratingList[i].getRating()}"
        ratingTotal += ratingList[i].getRating()
    ratingString += f"\n\nAll ratings totaled to {ratingTotal} overall!"
    messagebox.showinfo(title='Passenger Rating Report', message=f'{ratingString}')
    managerReport = open("flightReport", "w")
    managerReport.write(f'{ratingString}')
    managerReport.close()

def quitApp():
    login.destroy()
    managerWindow.destroy()
    sys.exit()


def changeSeat():
    name = simpledialog.askstring('Name', "What is the name printed on your ticket?", parent=passengerWindow)
    if name is not None:
        first, last = name.split(" ")
        seatNumber = int(simpledialog.askfloat('Seat', "Which seat are you currently assigned to?\n(Please enter in a numeric value)", parent=passengerWindow))
        if seatNumber is not None:
            requestedSeat = int(simpledialog.askfloat('New Seat', "Which seat would you liked to be moved to?\n(Please enter a numeric value)", parent=passengerWindow))
            if requestedSeat is not None:
                if app.seatList[requestedSeat - 1].isOpen:
                    if app.seatList[seatNumber-1].passenger.getFirst() == first and app.seatList[seatNumber-1].passenger.getLast() == last:
                        app.seatList[seatNumber - 1].isOpen = True
                        app.seatList[seatNumber - 1].passenger = None
                        passengerViewButtons[seatNumber - 1].config(bg='green')
                        managerViewButtons[seatNumber - 1].config(bg='green')
                        if os.path.exists(f"_Tickets/ Seat {seatNumber:03}, {last}"):
                            os.remove(f"_Tickets/ Seat {seatNumber:03}, {last}")

                        editPassenger = Passenger(first, last, "None", 0)
                        app.seatList[requestedSeat - 1].addPassenger(editPassenger)
                        passengerViewButtons[requestedSeat - 1].config(bg='red')
                        managerViewButtons[requestedSeat - 1].config(bg='red')
                        generateTickets([editPassenger], [requestedSeat])
                        messagebox.showinfo(title='Update', message='Your seat has been updated!')
                    else:
                        messagebox.showwarning(title='Update',
                                               message='The name does not match who is currently seated.')
                else:
                    messagebox.showwarning(title='Update', message='That seat is unavailable.')


def loginButton():
    if usernameBox.get() == managerPhrase:
        managerWindow.deiconify()
        mP.withdraw()
    usernameBox.delete(0, END)


def bookSeat():
    categoryScreen.deiconify()


def passengerLogin():
    login.withdraw()
    passengerWindow.deiconify()


def managerLogin():
    login.withdraw()
    mP.deiconify()


def logout():
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
    for i in range(1, 120 + 1):
        b = Button(master, text=f"{i}", bg='green', fg='white', width=2, height=1)
        seatList.append(b)
        b.place(x=x, y=y)
        x += 23
        if i % 3 == 0:
            if i % 6 == 0:
                x -= 161
                y += 25
            else:
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

chooseCat = Button(categoryScreen, text='Select Category', bg='blue', fg='white', command=lambda: chooseCategory())
chooseCat.place(x=400, y=400)
# -----------------------------------------------------------------------------------------------------------------


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
