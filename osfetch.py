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

    # Running Processes (Top 5)
    processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_>
                       key=lambda p: p.cpu_percent() + p.memory_percent(), reverse>
    info['Top Processes'] = [f"{p.info['name']} (PID: {p.info['pid']})" for p in p>


    # Desktop Environment and Window Manager
    info['DE'] = os.environ.get('XDG_SESSION_DESKTOP', 'Unknown')
    info['WM'] = os.environ.get('DESKTOP_SESSION', 'Unknown')

    return info

