# Import libraries
from email.policy import default
import requests
import dearpygui.dearpygui as dpg
import json

# Setup OS window for Dear Py Gui
dpg.create_context()
dpg.create_viewport(title='Network Development and Debugging Toolkit', width=1280, height=720)

# global variables for handling things such as the currently selected method
method = ""

methods = ["POST", "GET"]
parameters = []
parameter = ""

# Used for changing the currently selected method
def set_method(sender):
    global method
    method = dpg.get_value(sender)

# The Main function to test the API
def API_test(sender, data, user_data):
    if method == "GET":
        request = requests.get(dpg.get_value("URL"))
        request_json = json.loads(request.text)
        response_data = ""
        for k, v in request_json.items():
            response_data += f'{k} : {v}\n\n'
        
        dpg.configure_item("Response", default_value=response_data)

# Adds a parameter to the list box and the global array
def add_parameter(sender, data, user_data):
    global parameters
    parameters.append(f'{dpg.get_value("Parameter")}:{dpg.get_value("Value")}')
    dpg.configure_item("Parameters", items=parameters)

# sets the currently selected parameter
def set_parameter(sender):
    global parameter
    parameter = dpg.get_value(sender)

# Deletes the selected parameter from the parameters listbox
def delete_parameter(sender, data, user_data):
    global parameter, parameters
    parameters.remove(parameter)
    dpg.configure_item("Parameters", items=parameters)

# API Test Window
with dpg.window(label="API Test", width=300, height=600, no_close=True):
    dpg.add_text("API Test Tool")

    dpg.add_input_text(label="URL", tag="URL")

    dpg.add_listbox(label="Parameters", tag="Parameters", callback=set_parameter)

    dpg.add_button(label="Remove Parameter", callback=delete_parameter)

    # Using this as a line break similar to <br> in HTML
    dpg.add_text()

    dpg.add_listbox(label="Method", items=methods, callback=set_method)
    dpg.add_button(label="Send", callback=API_test)
    dpg.add_text()
    dpg.add_text("Response:")
    dpg.add_input_text(tag="Response", multiline=True, readonly=True, height=250, width=284)

# Add Parameter Window so the user can add parameters to the request
with dpg.window(label="Add Parameter", width=300, height=200, pos=[300,0], no_close=True):
    dpg.add_text("Add Parameter")
    dpg.add_input_text(label="Parameter", tag="Parameter")
    dpg.add_input_text(label="Value", tag="Value")
    dpg.add_button(label="Add", callback=add_parameter)

# Run the application
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()

dpg.destroy_context()