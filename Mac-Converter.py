import os
import sys
import uuid
import socket
import time
import re 

mac_address = ""

with open("mac-list.txt", "a") as mac_list:
    mac_list.write("\n" + time.strftime("%m/%d/%Y") + "\n\n")
    time.sleep(0.5)

print ("\nThis program converts between Cisco and PC formatted MAC addresses and stores the results in a file called \"Mac-List\"\n\n")

def is_valid_mac(mac):
    return re.match("([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", mac) or re.match("([0-9A-Fa-f]{4}\.){2}([0-9A-Fa-f]{4})$", mac)

def convert_to_cisco(mac):
    mac = mac.lower().replace(":", "").replace("-", "")
    return mac[0:4] + "." + mac[4:8] + "." + mac[8:12]

def convert_to_pc(mac):
    mac = mac.upper().replace(".", "")
    return mac[0:2] + ":" + mac[2:4] + ":" + mac[4:6] + ":" + mac[6:8] + ":" + mac[8:10] + ":" + mac[10:12]

def append_to_file(mac):
    with open("mac-list.txt", "a") as mac_list:
        mac_list.write(mac + "\n")

def main():
    while True:
        mac_address = input("Please enter a MAC address, or \"q\" for quit: ")
        if mac_address.lower() == "q":
            print("\nThe converted MAC addresses are stored in the file \"Mac-List\".")
            break
        if not is_valid_mac(mac_address):
            print("\n\n== That is not a valid MAC address ==\n\n")
            continue

        if ":" in mac_address or "-" in mac_address:
            converted_mac = convert_to_cisco(mac_address)
            print("\nThe Cisco MAC address is: " + converted_mac + "\n")
            append_to_file(converted_mac)
        elif "." in mac_address:
            converted_mac = convert_to_pc(mac_address)
            print("\nThe PC MAC address is: " + converted_mac + "\n")
            append_to_file(converted_mac)

if __name__ == "__main__":
    main()

with open("mac-list.txt", "r") as mac_list:
    mac_list_read = mac_list.read()
    print("With the file contents:\n\n" + mac_list_read)
print("\n\nQuitting...")  
time.sleep(5)
sys.exit()
