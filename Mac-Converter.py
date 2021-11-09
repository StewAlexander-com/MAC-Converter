import os
import sys
import uuid
import socket
import time

#Variable for storring the MAC address
mac_address = ""

#open the file mac-list.txt and add the date
with open("mac-list.txt", "a") as mac_list:
    mac_list.write("\n" + time.strftime("%m/%d/%Y") + "\n\n")
    #sleep for 0.5 seconds
    time.sleep(0.5)
    #close the file
    mac_list.close()

print ("\nThis program converts between Cisco and PC formatted MAC addresses and stores the results in a file called \"Mac-List\"\n\n")

while mac_address != "q":
    #request the mac address from the user
    mac_address = input("Please enter a MAC address, or \"q\" for quit: ")
    #if the mac address has ":" or "-" in it, then it's a PC address
    if ":" in mac_address or "-" in mac_address:
        #convert the mac address to cisco format
        #save mac_address as lowecase
        mac_address = mac_address.lower()
        #remove the ":" from the mac_address
        mac_address = mac_address.replace(":", "")
        #remove the "-" from the mac_address
        mac_address = mac_address.replace("-", "")
        #Every 4 characters, insert a "."
        mac_address = mac_address[0:4] + "." + mac_address[4:8] + "." + mac_address[8:12]
        #print the mac address
        print("\nThe Cisco MAC address is: " + mac_address + "\n")
        #append the mac address to a file named "mac-list"
        with open("mac-list.txt", "a") as mac_list:
            mac_list.write(mac_address + "\n")
    #if the mac address has "." then it's a Cisco address   
    elif "." in mac_address:
        #convert the mac address to PC format
        #save mac_address as uppercase
        mac_address = mac_address.upper()
        #remove the "." from the mac_address
        mac_address = mac_address.replace(".", "")
        #Every 2 characters, insert a ":"
        mac_address = mac_address[0:2] + ":" + mac_address[2:4] + ":" + mac_address[4:6] + ":" + mac_address[6:8] + ":" + mac_address[8:10] + ":" + mac_address[10:12]
        #print the mac address
        print("\nThe PC MAC address is: " + mac_address+ "\n")
        #append the mac address to a file named "mac-list"
        with open("mac-list.txt", "a") as mac_list:
            mac_list.write(mac_address + "\n")
    #if the mac address has no "." or ":" or "q" or number of character !=14 or 1 then its not a valid MAC address
    elif "." not in mac_address and ":" not in mac_address and mac_address != "q" and len(mac_address) != 14 and len(mac_address) != 1:
        #print the error message
        print("\n\n== That is not a valid MAC address ==\n\n")
    elif mac_address == "q":
        #print the message
        print("\nThe converted MAC addresses are stored in the file \"Mac-List\",")
    else :
        break

#print the contents of the file "Mac-List.txt" to the screen
with open("mac-list.txt", "r") as mac_list:
    #read the file
    mac_list_read = mac_list.read()
    #print the file contents
    print("With the file contents:\n\n" + mac_list_read)
print("\n\nQuitting...")  
#close the file
mac_list.close()
#sleep for 5 seconds
time.sleep(5)
#exit the program
sys.exit()
