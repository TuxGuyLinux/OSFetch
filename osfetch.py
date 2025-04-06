import platform
import psutil
import subprocess
import os
import argparse

def get_system_info():
    """Gathers and returns detailed system information."""

    info = {}
    info['OS'] = platform.system()
    info['OS Release'] = platform.release()
    info['Kernel'] = platform.version()
    info['Architecture'] = platform.machine()
    info['CPU'] = platform.processor()
    info['Memory'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3), 2)) >

    # Disk Usage
    disk_usage = psutil.disk_usage('/')
    info['Disk Total'] = str(round(disk_usage.total / (1024.0 ** 3), 2)) + " GB"
    info['Disk Used'] = str(round(disk_usage.used / (1024.0 ** 3), 2)) + " GB"
    info['Disk Free'] = str(round(disk_usage.free / (1024.0 ** 3), 2)) + " GB"

    # Desktop Environment and Window Manager
    info['DE'] = os.environ.get('XDG_SESSION_DESKTOP', 'Unknown')
    info['WM'] = os.environ.get('DESKTOP_SESSION', 'Unknown')

    return info

def display_os_icon(os_name):
    """Displays an ASCII art icon for the OS."""

    os_name = os_name.lower()
    if "linux" in os_name:
        print("""
        \\   /\\
         \\ /
          O
         / \\
        /   \\
        """)
    elif "windows" in os_name:
        print("""
        +------+------+
        |      |      |
        +------+------+
        |      |      |
        +------+------+
        """)
    elif "darwin" in os_name:
        print("""
             @@@@@@@@
          @@@@@@@@@@@@
        @@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@
             @@@@@@@@
        """)
    else:
        print("Unknown OS Icon")

def display_system_info(info, show_icon=False):
    """Displays the system information in a formatted way."""

    if show_icon:
        display_os_icon(info['OS'])

    print("System Information:")
    print("-" * 30)
    for key, value in info.items():
        if isinstance(value, list):
            print(f"{key}:")
            for item in value:
                print(f"  - {item}")
        else:
            print(f"{key}: {value}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display system information.")
    parser.add_argument("-i", "--icon", action="store_true", help="Display OS icon")
    args = parser.parse_args()

    system_info = get_system_info()
    display_system_info(system_info, show_icon=args.icon)

