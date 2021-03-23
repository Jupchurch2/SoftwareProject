from tkinter import *

root = Tk()
login = Toplevel()

root.geometry('650x400')
root.title('Seating App')

login.geometry('325x200')
login.title('Login')
login.config(bg='grey')

usernameBox = Entry(login, width=30)
usernameBox.pack()


def quitApp():
    login.destroy()
    root.destroy()
    sys.exit()

def loginButton():
    loginLabel = Label(root)
    if usernameBox.get() == 'Manager':
        root.deiconify()
        login.withdraw()


def logout():
    login.deiconify()
    root.withdraw()


button = Button(login, text="Login", padx=20, pady=10, command=lambda: loginButton())
button.pack()

quitButton = Button(login, text='Exit', command=lambda: quitApp())
quitButton.pack()

logoutButton = Button(root, text='Log Out', command=lambda: logout())
logoutButton.pack()
# Creating an event loop
root.withdraw()
root.mainloop()
