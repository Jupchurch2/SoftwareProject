from tkinter import *

# -----------------------------------------------------------------------------------------------------------------

managerWindow = Tk()
login = Toplevel()
passengerWindow = Toplevel()
mP = Toplevel()
reportScreen = Toplevel()
ticketScreen = Toplevel()

# -----------------------------------------------------------------------------------------------------------------

mbHEIGHT = 6
mbWIDTH = 30
window = '800x800'
planeImage = PhotoImage(file='planelayout_New.png')
managerPhrase = 'ManagerLogin'
categories = ['Business', 'Tourist', 'Family']
clicked = StringVar()
clicked.set(categories[0])

managerViewButtons = []
passengerViewButtons = []
seatX = 330
seatY = 160

# -----------------------------------------------------------------------------------------------------------------

ticketScreen.geometry(window)
ticketScreen.title('Book Your Seat!')

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

usernameBox = Entry(mP, width=30, show='*')
usernameBox.place(relx=.4, rely=.3)

nameBox = Entry(ticketScreen, width=30)
nameBox.place(relx=.4, rely=.25)

categoryBox = OptionMenu(ticketScreen, clicked, *categories,)
categoryBox.place(relx=.4, rely=.3)

def bookTicket():
    ticketScreen.withdraw()


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
    ticketScreen.deiconify()


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
bookButton = Button(ticketScreen, text='Book', bg='blue', fg='white', command=lambda: bookTicket()).place(x=740, y=770)

reportButton = Button(managerWindow, text='Print Report', bg='blue', fg='white').place(x=5, y=770)

ticketButton = Button(passengerWindow, text='Book a seat', bg='blue', fg='white', command=lambda: bookSeat()).place(x=5, y=770)

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
ticketScreen.withdraw()

# Creating an event loop
managerWindow.mainloop()
