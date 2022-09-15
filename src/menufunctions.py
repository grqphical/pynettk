#####################################################
# Script for handling the menu functions of the app
#####################################################

import requests
import dearpygui.dearpygui as dpg
import json

# Function for toggling the webserver test window
def webservertestview(sender):
    dpg.configure_item("Webserver Test Tool", show=dpg.get_value(sender))