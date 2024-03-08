# Project Team 3 (Alexander Smith, Daniel Smith, John Sharp)
# Ivy Tech Asset Manager - Detect OS Theme
# Returns either "light" or "dark" based on the OS theme, defaulting to "light" if detection is unsuccessful

import os
import subprocess
import platform

def get_os_theme():
    # Determine the OS
    os_name = platform.system()

    # Windows detection logic
    if os_name == "Windows":
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            return "dark" if value == 0 else "light"
        except FileNotFoundError:
            return "light"  # Default to light if unable to determine
    # macOS detection logic
    elif os_name == "Darwin":
        
        try:
            mode = subprocess.check_output(['defaults', 'read', '-g', 'AppleInterfaceStyle'], text=True)
            return "dark" if mode.strip() == 'Dark' else "light"
        except subprocess.CalledProcessError:
            return "light"  # Default to light if unable to determine
    else:
        return "light"  # Default to light for unsupported OS
