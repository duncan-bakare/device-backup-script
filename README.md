# Cisco Device Backup Automation

A lightweight Python script that automates backing up running configurations from Cisco network devices using SSH.  
This project demonstrates practical **network automation** skills with **Netmiko**, **Python**, and **file handling**.

---

## 🚀 Overview

Manually logging into multiple routers or switches to copy configurations is time-consuming and error-prone.  
This script connects to each device listed in a `.csv` file, retrieves its `show running-config` output, and saves it as a timestamped text file inside a `backups/` folder.

It’s ideal for learning **Python-based network automation**, a skill highly valued in large-scale infrastructure roles such as those at Meta, Google, and AWS.

---

## 🧠 Features
- SSHs into multiple Cisco devices automatically  
- Saves each configuration as a timestamped `.txt` backup  
- Organizes backups in a dedicated folder  
- Handles connection errors gracefully  
- Easily extendable for multi-vendor networks  

---

## 🗂️ Project Structure
