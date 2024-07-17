##############################################################################
# 
#   This is a simple app template that uses the 
#   customtkinter module to create a custom tkinter 
#   window with a sidebar.pystray is used for the 
#   system tray icon, and menu.
# 
#   @Author: BeardyMike
# 
##############################################################################



##############################################################################
# import modules
import customtkinter
import pystray
from PIL import Image
##############################################################################



##############################################################################
# Global variables

# temp variable to store the previous event for the hover function
temp = ""

# Define the image for the system tray icon
image = Image.open("logo.ico")
##############################################################################



##############################################################################
# Functions and Commands

# Function to compare the current event to the previous event
def compare(event, temp):
    return event == temp

# Function to print to the console when a button is hovered over
# add      .bind("<Enter>", lambda eff: on_hover(eff="None", event="Button Name"), add='+')     to something to call this function
def on_hover(eff="None", event=""):
    global temp
    if compare(event, temp) == True:
        return
    print("Hovering over " + event)
    temp = event
    return

# Function to quit the app, called when the Quit option is selected from the system tray icon menu
def quit_window():
    icon.stop()
    app.quit()

# Function to hide the window, called when the window is closed
def withdraw_window():
    app.withdraw()

# Function to toggle the window, called when the .Starter option is chosen from the system tray
def toggle_window():
    if app.state() == "withdrawn":
        app.deiconify()
    else:
        app.withdraw()
##############################################################################



##############################################################################
# Classes

# This class will be the main app window
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("")
        self.resizable(False, False)    

        # Configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=120, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")


        # Create the logo label, and bind it to the left, middle, and right mouse buttons with lambda functions that print to the console
        self.image = Image.open("img.png")
        self.photo = customtkinter.CTkImage(self.image, size=(934/10,330/10))
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, image=self.photo, text="")
        self.logo_label.bind('<Button-1>', lambda e: print("The logo was clicked with the left mouse button"), add='+')
        self.logo_label.bind('<Button-2>', lambda p: print("The logo was clicked with the middle mouse button"), add='+')
        self.logo_label.bind('<Button-3>', lambda p: print("The logo was clicked with the right mouse button"), add='+')
        self.logo_label.bind("<Enter>", lambda eff: on_hover(eff="None", event="the app logo"), add='+')
        self.logo_label.grid(row=0, column=0, padx=20, pady=25)

        # Create the sidebar buttons, each with a command that prints to the console
        # Scanner Button
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Scanner", command=lambda:print("Scanner Button Pressed"))
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_1.bind("<Enter>", lambda eff: on_hover(eff="None", event="Scanner Button"), add='+')

        # Contact Button
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Contact", command=lambda:print("Contact Button Pressed"))
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_2.bind("<Enter>", lambda eff: on_hover(eff="None", event="Contact Button"), add='+')

        # Remote Button
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Remote", command=lambda:print("Remote Button Pressed"))
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_3.bind("<Enter>", lambda eff: on_hover(eff="None", event="Remote Button"), add='+')

        # Subscription Button
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Subscription", command=lambda:print("Subscription Button Pressed"))
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_4.bind("<Enter>", lambda eff: on_hover(eff="None", event="Subscription Button"), add='+')

        # Account Button
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, text="Account", command=lambda:print("Account Button Pressed"))
        self.sidebar_button_5.grid(row=6, column=0, padx=20, pady=(30,10))
        self.sidebar_button_5.bind("<Enter>", lambda eff: on_hover(eff="None", event="Account Button"), add='+')
##############################################################################



##############################################################################
# Main
#
# Create the system tray icon, with a menu that has two options: Quit and Show
icon = pystray.Icon(".Starter", image, title=".Starter", menu=pystray.Menu(pystray.MenuItem(".Starter", toggle_window, default=True),pystray.MenuItem("Quit", quit_window)))
#
# Run the system tray icon in the background, detached from the main app. this way the icon will continue to run even if the main app is closed.
icon.run_detached()
#
# Create the main app, this will be the main window that is shown when the Show option is selected from the system tray icon menu
app = App()
#
# Set the size of the app window
app.geometry("650x350")
#
# Set the icon for the app, using logo.ico as the icon file
app.iconbitmap("logo.ico")
#
# When the window is closed, call the withdraw_window function, this way the window is not destroyed.
app.protocol('WM_DELETE_WINDOW', withdraw_window)
#
# Start the main app
# app.withdraw()
app.mainloop()
#
##############################################################################
