import psutil
from datetime import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

cpu = psutil.cpu_percent()
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print("System Health Report")
print("----------------------")
print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")
print(f"Disk Usage: {disk}%")

if cpu > CPU_THRESHOLD:
    print("ALERT: High CPU Usage!")

if memory > MEMORY_THRESHOLD:
    print("ALERT: High Memory Usage!")

if disk > DISK_THRESHOLD:
    print("ALERT: High Disk Usage!")

print("\nRunning Processes:")
for process in psutil.process_iter(['pid', 'name']):
    print(process.info)