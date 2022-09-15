#####################################################
# Script for the GUI and primary app functions
#####################################################

# Import libraries
import apitest
import requests
import dearpygui.dearpygui as dpg
import json

# Setup OS window for Dear Py Gui
dpg.create_context()
dpg.create_viewport(title='Network Development and Debugging Toolkit', width=1280, height=720)

# API Test Window
with dpg.window(label="API Test", width=300, height=600, no_close=True):
    dpg.add_text("API Test Tool")

    dpg.add_input_text(label="URL", tag="URL")

    dpg.add_listbox(label="Parameters", tag="Parameters", callback=apitest.set_parameter)

    dpg.add_button(label="Remove Parameter", callback=apitest.delete_parameter)

    # Using this as a line break similar to <br> in HTML
    dpg.add_text()

    dpg.add_listbox(label="Method", items=apitest.methods, callback=apitest.set_method)
    dpg.add_button(label="Send", callback=apitest.API_test)
    dpg.add_text()
    dpg.add_text("Status Code:")
    dpg.add_text(tag="StatusCode")
    dpg.add_text("Response:")
    dpg.add_input_text(tag="Response", multiline=True, readonly=True, height=250)

# Add Parameter Window so the user can add parameters to the request
with dpg.window(label="Add Parameter", width=300, height=200, pos=[300,0], no_close=True):
    dpg.add_text("Add Parameter")
    dpg.add_input_text(label="Parameter", tag="Parameter")
    dpg.add_input_text(label="Value", tag="Value")
    dpg.add_button(label="Add", callback=apitest.add_parameter)

# Run the application
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()

dpg.destroy_context()