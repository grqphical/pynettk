###########################################################
# Script for handling the Webserver testing part of the app
###########################################################

import requests
import dearpygui.dearpygui as dpg
import json

# global variables for handling things such as the currently selected method
method = "POST"

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
        response_data = ""
        try:
            request_json = request.json()
            for k, v in request_json.items():
                response_data += f'{k} : {v}\n\n'
        except:
            pass
        
        dpg.configure_item("Response", default_value=response_data)
        dpg.configure_item("Ping", default_value=request.elapsed / 1000)
        if request.status_code >= 200 and request.status_code < 300:
            dpg.configure_item("StatusCode", default_value=request.status_code, color=[0,255,0])
        elif request.status_code >= 400 and request.status_code < 600:
            dpg.configure_item("StatusCode", default_value=request.status_code, color=[255,0,0])
        else:
            dpg.configure_item("StatusCode", default_value=request.status_code)
    elif method == "POST":
        request = requests.get(dpg.get_value("URL"))
        response_data = ""
        try:
            request_json = request.json()
            for k, v in request_json.items():
                response_data += f'{k} : {v}\n\n'
        except:
            pass
        
        dpg.configure_item("Response", default_value=response_data)
        if request.status_code >= 200 and request.status_code < 300:
            dpg.configure_item("StatusCode", default_value=request.status_code, color=[0,255,0])
        elif request.status_code >= 400 and request.status_code < 600:
            dpg.configure_item("StatusCode", default_value=request.status_code, color=[255,0,0])
        else:
            dpg.configure_item("StatusCode", default_value=request.status_code)

# Adds a parameter to the list box and the global array
def add_parameter(sender, data, user_data):
    global parameters
    parameters.append(f'{dpg.get_value("Parameter")}:{dpg.get_value("Value")}')
    dpg.configure_item("Parameters", items=parameters)
    parameter = f'{dpg.get_value("Parameter")}:{dpg.get_value("Value")}'

# sets the currently selected parameter
def set_parameter(sender):
    global parameter
    parameter = dpg.get_value(sender)

# Deletes the selected parameter from the parameters listbox
def delete_parameter(sender, data, user_data):
    global parameter, parameters
    parameters.remove(parameter)
    dpg.configure_item("Parameters", items=parameters)

# Open the Add Parameter window
def open_parameter_window(sender, data, user_data):
    dpg.configure_item("AddParameter", show=True)