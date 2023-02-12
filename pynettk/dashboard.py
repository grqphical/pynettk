import dearpygui.dearpygui as dpg
from threading import Thread
import requests
import time

sites = []
dashboard_data = []
selected_site = ""

def UpdateDashboard():
    while True:
        global dashboard_data, sites
        for i in sites:
            if i == '':
                continue
            request = requests.get(i)
            dashboard_data.append(f'{i} | {request.status_code}')
        dpg.configure_item("Sites", items=dashboard_data)
        time.sleep(1)
        dashboard_data = []

def LoadAddSiteWindow(sender):
    dpg.configure_item("AddSite", show=True)

def AddSite(sender):
    url = dpg.get_value("AddSite.URL")
    sites.append(url)
    dpg.configure_item("AddSite", show=False)
    with open(".sites", "a") as file:
        file.write(f'{url};')

def InitDashboard():
    with open(".sites", "r") as file:
        data = file.read()
        sites_list = data.split(";")
        global sites
        sites = sites_list
    
    update_thread = Thread(target=UpdateDashboard)
    update_thread.daemon = True
    update_thread.start()

def SelectSite(sender):
    global selected_site
    print(dpg.get_value(sender))
    selected_site = dpg.get_value(sender).replace(" ", "").split("|")[0]

def RemoveSite(sender):
    global dashboard_data, sites
    for i in dashboard_data:
        if i.startswith(selected_site):
            dashboard_data.remove(i)
            with open(".sites", "w+") as file:
                for line in file:
                    file.write(line.replace(f'{i};', ''))
    dpg.configure_item("Sites", items=dashboard_data)
    sites.remove(selected_site)
    
