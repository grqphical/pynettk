#####################################################
# Script for handling the menu functions of the app
#####################################################

import dearpygui.dearpygui as dpg
import webbrowser

# Function for toggling the webserver test window
def webservertestview(sender):
    dpg.configure_item("Webserver Test Tool", show=dpg.get_value(sender))

# Show the about window
def show_about(sender):
    dpg.configure_item("About", show=True)

# Open the project's GitHub
def open_github(sender):
    webbrowser.open("https://github.com/grqphical07/pynettk")