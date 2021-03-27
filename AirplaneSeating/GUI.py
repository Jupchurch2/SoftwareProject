from tkinter import *
from tkinter import simpledialog

# -----------------------------------------------------------------------------------------------------------------

managerWindow = Tk()
login = Toplevel()
passengerWindow = Toplevel()
mP = Toplevel()

mbHEIGHT = 6
mbWIDTH = 30
window = '800x800'
planeImage = PhotoImage(file='planelayout_New.png')
managerPhrase = 'ManagerLogin'

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

# -----------------------------------------------------------------------------------------------------------------

usernameBox = Entry(mP, width=30, show='*')
usernameBox.place(relx=.4, rely=.3)


def quitApp():
    login.destroy()
    managerWindow.destroy()
    sys.exit()


def loginButton():
    if usernameBox.get() == managerPhrase:
        managerWindow.deiconify()
        mP.withdraw()
    usernameBox.delete(0, END)


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

planeLabel = Label(passengerWindow, image=planeImage)
planeLabel.place(x=175, y=30)

passengerViewButtons = []
x = 330
y = 160

for i in range(1, 120 + 1):
    b = Button(passengerWindow, text=f"{i}", bg='green', fg='white', width=2, height=1)
    passengerViewButtons.append(b)
    b.place(x=x, y=y)
    x += 23
    if i % 3 == 0:
        if i % 6 == 0:
            x -= 161
            y += 25
        else:
            x += 23

# -----------------------------------------------------------------------------------------------------------------

mP.bind('<Return>', loginButton)

button = Button(login, text="Passenger", height=mbHEIGHT, width=mbWIDTH, command=lambda: passengerLogin())
button.place(relx=.363, rely=.2)

mButton = Button(login, text='Manager', height=mbHEIGHT, width=mbWIDTH, command=lambda: managerLogin())
mButton.place(relx=.363, rely=.4)

mPB = Button(mP, text="Enter", command=lambda: loginButton()).place(relx=.49, rely=.34)

quitButton = Button(login, text='Exit', height=3, width=15, command=lambda: quitApp())
quitButton.place(relx=.43, rely=.87)

logoutButton = Button(managerWindow, text='Log Out', command=lambda: logout())
logoutButton.place(x=740, y=770)

logoutButton2 = Button(passengerWindow, text='Exit', width=6, fg='red', command=lambda: logout())
logoutButton2.place(x=740, y=770)

# Creating an event loop
managerWindow.withdraw()
passengerWindow.withdraw()
mP.withdraw()
managerWindow.mainloop()
