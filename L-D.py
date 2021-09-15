from winreg import *
from datetime import datetime

#Get the system and app dark mode values
PATH = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize'
key = OpenKey(HKEY_CURRENT_USER, PATH, 0, KEY_ALL_ACCESS ) #Opens the key/folder to the themes config files
valueSystem = EnumValue(key, 3)[1] #View the value in config file of the given key/folder
valueApps = EnumValue(key,2)[1]

def dark_mode():
    SetValueEx(key, 'AppsUseLightTheme', 0, REG_DWORD, 0)
    SetValueEx(key, 'SystemUsesLightTheme', 0, REG_DWORD, 0)

def light_mode():
    SetValueEx(key, 'AppsUseLightTheme', 0, REG_DWORD, 1)
    SetValueEx(key, 'SystemUsesLightTheme', 0, REG_DWORD, 1)

if valueSystem == 1 and valueApps == 1:
    dark_mode()
else:
    light_mode()