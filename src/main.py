#####################################################
# Script for the GUI and primary app functions
#####################################################

# Import libraries
import webservertest
import menufunctions as mf
import dearpygui.dearpygui as dpg


# Setup OS window for Dear Py Gui
dpg.create_context()
dpg.create_viewport(title='pynettk - Network Development and Debugging Toolkit', width=1280, height=720)

# Load Resources
width, height, channels, logo = dpg.load_image("resources/logo.png")
with dpg.texture_registry():
    dpg.add_static_texture(width=512, height=512, default_value=logo, tag="logo")

# Create menu bar on the window
with dpg.viewport_menu_bar():
    with dpg.menu(label="View"):
        dpg.add_menu_item(label="Webserver Test", check=True, callback=mf.webservertestview, default_value=True)
        dpg.add_menu_item(label="About", callback=mf.show_about)

    with dpg.menu(label="Settings"):
        dpg.add_menu_item(label="Style Settings")
        dpg.add_menu_item(label="App Settings")

# API Test Window
with dpg.window(label="Webserver Test Tool", width=300, height=600, no_close=True, tag="Webserver Test Tool"):
    dpg.add_text("Webserver Test Tool")

    dpg.add_input_text(label="URL", tag="URL")

    dpg.add_listbox(label="Parameters", tag="Parameters", callback=webservertest.set_parameter)

    dpg.add_button(label="Add Parameter", callback=webservertest.open_parameter_window)
    dpg.add_button(label="Remove Parameter", callback=webservertest.delete_parameter)
    

    # Using this as a line break similar to <br> in HTML
    dpg.add_text()

    dpg.add_listbox(label="Method", items=webservertest.methods, callback=webservertest.set_method)
    dpg.add_button(label="Send", callback=webservertest.API_test)
    dpg.add_text()
    dpg.add_text("Status Code:")
    dpg.add_text(tag="StatusCode")
    dpg.add_text("Ping:")
    dpg.add_text(tag="Ping")
    dpg.add_text("Response:")
    dpg.add_input_text(tag="Response", multiline=True, readonly=True, height=250)

# Add Parameter Window so the user can add parameters to the request
with dpg.window(label="Add Parameter", width=300, height=200, pos=[300,0], show=False, tag="AddParameter"):
    dpg.add_text("Add Parameter")
    dpg.add_input_text(label="Parameter", tag="Parameter")
    dpg.add_input_text(label="Value", tag="Value")
    dpg.add_button(label="Add", callback=webservertest.add_parameter)

# Create the about window ahead of time
with dpg.window(label="About pynettk", tag="About", show=False):
    dpg.add_image("logo", width=128, height=128)
    dpg.add_text("pynettk - Network Debugging and Development Kit")
    dpg.add_text()
    dpg.add_text("Version: 0.1.00")
    dpg.add_text("Created by: grqphical")
    dpg.add_text("")
    dpg.add_button(label="Github", callback=mf.open_github)

# Run the application
dpg.set_viewport_small_icon("resources/logo.ico")
dpg.set_viewport_large_icon("resources/logo.ico")
dpg.show_style_editor()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()

dpg.destroy_context()