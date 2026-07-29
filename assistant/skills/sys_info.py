"""Skill: report system info — only what was asked for."""

import psutil


def run(command: str) -> str:
    if "battery" in command:
        battery = psutil.sensors_battery()
        if battery:
            return f"Battery is at {int(battery.percent)} percent."
        return "No battery detected."

    if "cpu" in command:
        cpu = psutil.cpu_percent(interval=1)
        return f"CPU usage is {cpu} percent."

    if "ram" in command or "memory" in command:
        ram = psutil.virtual_memory().percent
        return f"RAM usage is {ram} percent."

    if "system" in command:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        return f"CPU usage is {cpu} percent. RAM usage is {ram} percent."

    return "Say check battery, check cpu, check ram, or system status."