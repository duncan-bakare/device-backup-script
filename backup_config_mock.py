from unittest.mock import MagicMock
from datetime import datetime
import os
import csv

# Backup folder
backup_dir = "backups"
os.makedirs(backup_dir, exist_ok=True)

# Timestamp for filenames
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Read devices from CSV
with open("devices.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Connecting to {row['device_name']} ({row['host']})...")

        # Mock connection instead of real Netmiko
        connection = MagicMock()
        connection.send_command.return_value = f"show running-config simulated for {row['device_name']}"

        # "Backup" output
        output = connection.send_command("show running-config")
        filename = f"{backup_dir}/{row['device_name']}_{timestamp}.txt"
        with open(filename, "w") as backup:
            backup.write(output)

        print(f"✔ Backup saved: {filename}")

