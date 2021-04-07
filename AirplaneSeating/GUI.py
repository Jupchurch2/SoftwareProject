# Import all libraries to make the application functional
from tkinter import *
#from AppModel import *
#from Plane import *
#from Passenger import *

# -----------------------------------------------------------------------------------------------------------------

# Create all instance variables for the AppModel and the windows
#app = AppModel()

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

businessName = Entry(businessTicket, width=30)
businessName.place(relx=.4, rely=.25)

businessPref = Entry(businessTicket, width=10)
businessPref.place(relx=.4, rely=.5)

touristName1 = Entry(touristTicket, width=30)
touristName2 = Entry(touristTicket, width=30)
touristName1.place(x=.5, y=.45)
touristName2.place(x=.5, y=.65)

touristPref1 = Entry(touristTicket, width=10)
touristPref2 = Entry(touristTicket, width=10)
touristPref1.place(x=.5, y=.5)
touristPref2.place(x=.5, y=.7)

familyName1 = Entry(familyTicket, width=30)
familyName2 = Entry(familyTicket, width=30)
familyName3 = Entry(familyTicket, width=30)
familyName4 = Entry(familyTicket, width=30)
familyName5 = Entry(familyTicket, width=30)

familyPref1 = Entry(familyTicket, width=10)
familyPref2 = Entry(familyTicket, width=10)
familyPref3 = Entry(familyTicket, width=10)
familyPref4 = Entry(familyTicket, width=10)
familyPref5 = Entry(familyTicket, width=10)

familyName1.place(x=.5, y=.15)
familyName2.place(x=.5, y=.30)
familyName3.place(x=.5, y=.45)
familyName4.place(x=.5, y=.60)
familyName5.place(x=.5, y=.75)

familyPref1.place(x=.5, y=.2)
familyPref2.place(x=.5, y=.35)
familyPref3.place(x=.5, y=.5)
familyPref4.place(x=.5, y=.65)
familyPref5.place(x=.5, y=.8)

# Defining button functions
def bookTicket():
    fullName = businessName.get()
    first, last = fullName.split(' ')
    preference = businessPref.get()
    businessTicket.withdraw()
    # newPassenger = Passenger(first, last, category, preference)


def chooseCategory():
    category = clicked.get()
    if category == 'Business':
        businessTicket.deiconify()
    elif category == 'Tourist':
        touristTicket.deiconify()
    elif category == 'Family':
        familyTicket.deiconify()
    categoryScreen.withdraw()


def quitApp():
    login.destroy()
    managerWindow.destroy()
    sys.exit()


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
bookBusiness = Button(businessTicket, text='Book', bg='blue', fg='white', command=lambda: bookTicket()).place(x=740, y=770)

ticketButton = Button(passengerWindow, text='Book a seat', bg='blue', fg='white', command=lambda: bookSeat())
ticketButton.place(x=5, y=770)

chooseCat = Button(categoryScreen, text='Select Category', bg='blue', fg='white', command=lambda: chooseCategory())
chooseCat.place(x=400, y=400)
# -----------------------------------------------------------------------------------------------------------------
reportButton = Button(managerWindow, text='Print Report', bg='blue', fg='white').place(x=5, y=770)

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
