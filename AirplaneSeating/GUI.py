from tkinter import *

managerWindow = Tk()
login = Toplevel()
passengerWindow = Toplevel()

passengerWindow.geometry('650x400')
passengerWindow.title('Guest View')

managerWindow.geometry('650x400')
managerWindow.title('Manager View')

login.geometry('325x200')
login.title('Login')
login.config(bg='grey')

usernameBox = Entry(login, width=30)
usernameBox.pack()


def quitApp():
    login.destroy()
    managerWindow.destroy()
    sys.exit()

def loginButton():
    usernameText = Label(login, text=" ")
    if usernameBox.get() == 'Manager':
        managerWindow.deiconify()
        login.withdraw()
    elif usernameBox.get() == 'Guest' or 'guest':
        passengerWindow.deiconify()
        login.withdraw()
    else:
        usernameText.config(text='Invalid username', fg='red')
        usernameText.pack()
    usernameBox.delete(0, END)


def logout():
    login.deiconify()
    passengerWindow.withdraw()
    managerWindow.withdraw()


button = Button(login, text="Login", padx=20, pady=10, command=lambda: loginButton())
button.pack()

quitButton = Button(login, text='Exit', command=lambda: quitApp())
quitButton.pack()

logoutButton = Button(managerWindow, text='Log Out', command=lambda: logout())
logoutButton.pack()

logoutButton2 = Button(passengerWindow, text='Log Out', command=lambda: logout())
logoutButton2.pack()
# Creating an event loop

managerWindow.withdraw()
passengerWindow.withdraw()
managerWindow.mainloop()
