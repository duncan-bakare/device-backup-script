from netmiko import ConnectHandler
import csv
from datetime import datetime
import os

# Create backup directory if it doesn't exist
backup_dir = "backups"
os.makedirs(backup_dir, exist_ok=True)

# Timestamp for filenames
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Read devices from CSV file
with open("devices.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        device = {
            "device_type": row["device_type"],
            "host": row["host"],
            "username": row["username"],
            "password": row["password"],
        }

        print(f"Connecting to {row['device_name']} ({row['host']})...")
        try:
            connection = ConnectHandler(**device)
            output = connection.send_command("show running-config")
            connection.disconnect()

            filename = f"{backup_dir}/{row['device_name']}_{timestamp}.txt"
            with open(filename, "w") as backup:
                backup.write(output)
            
            print(f"✔ Backup saved: {filename}")

        except Exception as e:
            print(f"❌ Failed to back up {row['device_name']}: {e}")
