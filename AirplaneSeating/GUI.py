from tkinter import *

managerWindow = Tk()
login = Toplevel()
passengerWindow = Toplevel()
mP = Toplevel()

window = '800x800'

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

usernameBox = Entry(mP, width=30)
usernameBox.pack()

managerPhrase = 'ManagerLogin'

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


button = Button(login, text="Passenger", command=lambda: passengerLogin())
button.pack()

mButton = Button(login, text='Manager', command=lambda: managerLogin())
mButton.pack()

mPB = Button(mP, text="Enter", command=lambda: loginButton()).pack()

quitButton = Button(login, text='Exit', command=lambda: quitApp())
quitButton.pack()

logoutButton = Button(managerWindow, text='Log Out', command=lambda: logout())
logoutButton.pack()

logoutButton2 = Button(passengerWindow, text='Log Out', command=lambda: logout())
logoutButton2.pack()
# Creating an event loop

managerWindow.withdraw()
passengerWindow.withdraw()
mP.withdraw()
managerWindow.mainloop()
