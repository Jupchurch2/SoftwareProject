# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name:03}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(1, 121):
        file = open(f'_Tickets/ticket {i:03}; Last Name', "w")
        file.write("information")
        file.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
