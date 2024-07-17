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

# pip install customtkinter
import customtkinter

# pip install pystray
import pystray

from PIL import Image
import configparser
##############################################################################



##############################################################################
# Global variables

# temp variable to store the previous event for the hover function
temp = ""

# Define the image for the system tray icon
image = Image.open("logo.ico")

# Set the size of the main app window
gui_X = 650
gui_Y = 450
gui_sidebar_width = 140
gui_main_frame_width = gui_X - gui_sidebar_width
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

def ini_write(section, key, value):
    config = configparser.ConfigParser()
    config.read('data.ini')
    config.set(section, key, value) 
    with open('data.ini', 'w') as configfile:
        config.write(configfile)

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
main_frame_colour = ("#EBEBEB","#1A1A1A")

##############################################################################



##############################################################################
# Classes

# This class will be the main app window
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        def page1_button():
            print("Page 1 Button Pressed")
            self.main_frame.destroy()
            self.main_frame = Page1Frame(self)
            ini_write("main", "active_page", "1")

        def page2_button():
            print("Page 2 Button Pressed")
            self.main_frame.destroy()
            self.main_frame = Page2Frame(self)
            ini_write('main', 'active_page', "2") 
           
        def page3_button():
            print("Page 3 Button Pressed")
            self.main_frame.destroy()
            self.main_frame = Page3Frame(self)
            ini_write('main', 'active_page', "3") 
   
        def page4_button():
            print("Page 4 Button Pressed")
            self.main_frame.destroy()
            self.main_frame = Page4Frame(self)
            ini_write('main', 'active_page', "4") 

        def page5_button():
            print("Page 5 Button Pressed")
            self.main_frame.destroy()
            self.main_frame = Page5Frame(self)
            ini_write('main', 'active_page', "5") 
       
        # Configure window
        self.title("")
        self.resizable(False, False)
           

        # Configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        

        # Create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=gui_sidebar_width , corner_radius=0)
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
        # Page1 Button
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Page1", font=("Segoe UI", 16), command=page1_button)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_1.bind("<Enter>", lambda eff: on_hover(eff="None", event="Page1 Button"), add='+')

        # Page2 Button
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Page2", font=("Segoe UI", 16), command=page2_button)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_2.bind("<Enter>", lambda eff: on_hover(eff="None", event="Page2 Button"), add='+')

        # Page3 Button
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Page3", font=("Segoe UI", 16), command=page3_button)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_3.bind("<Enter>", lambda eff: on_hover(eff="None", event="Page3 Button"), add='+')

        # Page4 Button
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Page4", font=("Segoe UI", 16), command=page4_button)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_4.bind("<Enter>", lambda eff: on_hover(eff="None", event="Page4 Button"), add='+')

        # Page5 Button
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, text="Page5", font=("Segoe UI", 16), command=page5_button)
        self.sidebar_button_5.grid(row=6, column=0, padx=20, pady=(125,10))
        self.sidebar_button_5.bind("<Enter>", lambda eff: on_hover(eff="None", event="Page5 Button"), add='+')


            
        # Create page1_frame with widgets
        class Page1Frame(customtkinter.CTkFrame):
            def __init__(self, parent):
                super().__init__(parent, corner_radius=0, width=gui_main_frame_width, fg_color=main_frame_colour)
                self.grid(row=0, column=1, rowspan=5, sticky="nsew", padx=75)

                self.config = configparser.ConfigParser()
                self.config.read('data.ini')
                self.config.sections()

                # Create a blank label for row 1
                self.row1label = customtkinter.CTkLabel(self, text="")
                self.row1label.grid(row=0, column=1, padx=15, pady=25)

                # Create a slider
                self.sliderval = customtkinter.IntVar(value=1)
                self.slider = customtkinter.CTkSlider(self, number_of_steps=100, from_=0, to=1, command=lambda x: [self.progress1.set(self.slider.get()), self.progress2.set(self.slider.get()),print(self.slider.get()),ini_write('page1', 'slider', str(self.slider.get())) ], variable=self.sliderval)
                self.slider.set(float(self.config['page1']['slider']))
                self.slider.grid(row=1, column=1, padx=15, pady=20)

                # Create a progress bar that is linked to the slider
                self.progress1 = customtkinter.CTkProgressBar(self, orientation="horizontal")
                self.progress1.grid(row=2, column=1, padx=15, pady=20)
                self.progress1.set(self.slider.get())

                # Create a progress bar that is linked to the slider
                self.progress2 = customtkinter.CTkProgressBar(self, orientation="vertical")
                self.progress2.grid(row=1, column=2, rowspan=6, padx=50)
                self.progress2.set(self.slider.get())

                # Create a set of check boxes
                self.checkbox_var1 = customtkinter.StringVar(value=self.config['page1']['checkbox_var1'])
                self.checkbox_var2 = customtkinter.StringVar(value=self.config['page1']['checkbox_var2'])
                self.checkbox_var3 = customtkinter.StringVar(value=self.config['page1']['checkbox_var3'])

                self.checkbox1 = customtkinter.CTkCheckBox(self, text="CheckBox 1", font=("Segoe UI", 16),
                                                           command=lambda: [print("Checkbox1 checked") if self.checkbox_var1.get() == "on" else print("Checkbox1 unchecked"), ini_write('page1', 'checkbox_var1', self.checkbox_var1.get())],
                                                           variable=self.checkbox_var1, onvalue="on", offvalue="off")
                self.checkbox1.grid(row=3, column=1, padx=15, pady=15)

                self.checkbox2 = customtkinter.CTkCheckBox(self, text="CheckBox 2", font=("Segoe UI", 16),
                                                           command=lambda: [print("Checkbox2 checked") if self.checkbox_var2.get() == "on" else print("Checkbox2 unchecked"), ini_write('page1', 'checkbox_var2', self.checkbox_var2.get())],
                                                           variable=self.checkbox_var2, onvalue="on", offvalue="off")
                self.checkbox2.grid(row=4, column=1, padx=15, pady=15)

                self.checkbox3 = customtkinter.CTkCheckBox(self, text="CheckBox 3", font=("Segoe UI", 16),
                                                           command=lambda: [print("Checkbox3 checked") if self.checkbox_var3.get() == "on" else print("Checkbox3 unchecked"), ini_write('page1', 'checkbox_var3', self.checkbox_var3.get())],
                                                           variable=self.checkbox_var3, onvalue="on", offvalue="off")
                self.checkbox3.grid(row=5, column=1, padx=15, pady=15)

        # Create page2_frame with widgets, it has lots of buttons and labels
        class Page2Frame(customtkinter.CTkFrame):
            def __init__(self, parent):
                super().__init__(parent, corner_radius=0, width=gui_main_frame_width, fg_color=main_frame_colour)
                self.grid(row=0, column=1, rowspan=8, columnspan=2, sticky="nsew", padx=150)
                
                def set_active_button(button, button_name):
                    # Remove border from all buttons
                    for btn in [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6]:
                        btn.configure(border_color=main_frame_colour)
                    
                    # Set green border around the active button
                    if button_name != "6":
                        button.configure(border_color="green")
                    else:
                        button.configure(border_color="red")
                    
                    # Store the active button in the ini file
                    ini_write("page2", "active_button", button_name)

                # Create a blank label for row 1
                self.row1label = customtkinter.CTkLabel(self, text="")
                self.row1label.grid(row=0, column=1, padx=15, pady=25)
                # Create a set of buttons
                self.button1 = customtkinter.CTkButton(self, corner_radius=10, border_width=4, border_color=main_frame_colour, text="Button 1", font=("Segoe UI", 16), command=lambda: [set_active_button(self.button1, "1"), self.button6.configure(state="disabled", text="Disabled")])
                self.button1.grid(row=1, column=0, padx=15, pady=10)

                self.button2 = customtkinter.CTkButton(self, corner_radius=10, border_width=4, border_color=main_frame_colour, text="Button 2", font=("Segoe UI", 16), command=lambda: set_active_button(self.button2, "2"))
                self.button2.grid(row=2, column=0, padx=15, pady=10)

                self.button3 = customtkinter.CTkButton(self, corner_radius=10, border_width=4, border_color=main_frame_colour, text="Button 3", font=("Segoe UI", 16), command=lambda: set_active_button(self.button3, "3"))
                self.button3.grid(row=3, column=0, padx=15, pady=10)

                self.button4 = customtkinter.CTkButton(self, corner_radius=10, border_width=4, border_color=main_frame_colour, text="Button 4", font=("Segoe UI", 16), command=lambda: set_active_button(self.button4, "4"))
                self.button4.grid(row=4, column=0, padx=15, pady=10)

                self.button5 = customtkinter.CTkButton(self, corner_radius=10, border_width=4, border_color=main_frame_colour, text="Button 5", font=("Segoe UI", 16), command=lambda: [set_active_button(self.button5, "5"), self.button6.configure(state="normal", text="Button 6")])
                self.button5.grid(row=5, column=0, padx=15, pady=10)

                self.button6 = customtkinter.CTkButton(self, corner_radius=10, border_width=4, border_color=main_frame_colour, text="Disabled", font=("Segoe UI", 16), state="disabled", command=lambda: set_active_button(self.button6, "6"))
                self.button6.grid(row=6, column=0, padx=15, pady=10)

                # Read the active button from the ini file, and set the active button to the correct button
                config = configparser.ConfigParser()
                config.read('data.ini')
                active_button = config['page2']['active_button']
                if active_button == "1":
                    set_active_button(self.button1, "1")
                elif active_button == "2":
                    set_active_button(self.button2, "2")
                elif active_button == "3":
                    set_active_button(self.button3, "3")
                elif active_button == "4":
                    set_active_button(self.button4, "4")
                elif active_button == "5":
                    set_active_button(self.button5, "5")
                else:
                    set_active_button(self.button1, "1")
                


        # Create page3_frame with widgets
        class Page3Frame(customtkinter.CTkFrame):
            def __init__(self, parent):
                super().__init__(parent, corner_radius=0, width=gui_main_frame_width, fg_color=main_frame_colour)
                self.grid(row=0, column=1, rowspan=6, sticky="nsew", padx=25)

                # Create a blank label for row 1
                self.row1label = customtkinter.CTkLabel(self, text="This is Page 3", font=("Segoe UI", 36))
                self.row1label.grid(row=0, column=0, padx=15, pady=25)
        
        # Create page4_frame with widgets
        class Page4Frame(customtkinter.CTkFrame):
            def __init__(self, parent):
                super().__init__(parent, corner_radius=0, width=gui_main_frame_width, fg_color=main_frame_colour)
                self.grid(row=0, column=1, rowspan=6, sticky="nsew", padx=25)

                # Create a blank label for row 1
                self.row1label = customtkinter.CTkLabel(self, text="This is Page 4", font=("Segoe UI", 36))
                self.row1label.grid(row=0, column=0, padx=15, pady=25)

        # Create page5_frame with widgets
        class Page5Frame(customtkinter.CTkFrame):
            def __init__(self, parent):
                super().__init__(parent, corner_radius=0, width=gui_main_frame_width, fg_color=main_frame_colour)
                self.grid(row=0, column=1, rowspan=6, sticky="nsew", padx=25)

                # Create a blank label for row 1
                self.row1label = customtkinter.CTkLabel(self, text="This is Page 5", font=("Segoe UI", 36))
                self.row1label.grid(row=0, column=0, padx=15, pady=25)

        # read the active page from the ini file, and set the main frame to the correct page
        config = configparser.ConfigParser()
        config.read('data.ini')
        active_page = config['main']['active_page']
        if active_page == "1":
            self.main_frame = Page1Frame(self)
        elif active_page == "2":
            self.main_frame = Page2Frame(self)
        elif active_page == "3":
            self.main_frame = Page3Frame(self)
        elif active_page == "4":
            self.main_frame = Page4Frame(self)
        elif active_page == "5":
            self.main_frame = Page5Frame(self)
        else:
            self.main_frame = Page1Frame(self)



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
app.geometry(f"{gui_X}x{gui_Y}")
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
