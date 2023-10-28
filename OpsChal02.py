# 401 Ops Challenge 2
# Author: Samuel Allan
# Date of last revision: 10/02/2023
# Purpose:
# - In Python, create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.
# - Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# - Evaluate the response as either success or failure.
# - Assign success or failure to a status variable.
# - For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
# - Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8
# The script must:
# - Save the output to a text file as a log of events.
# - Accept user input for the target IP address.

# Import space
import os
import time
import datetime

# Variables
hostname = input("Provide an IP address: ")  # Storing the host in input for now
output_file = input("Provide a name for your text log: ")
numbah = input("Provide the length of time to run in minutes: ")
number = float(numbah)  # Convert to an integer

# Calculate the end time based on the current time and the specified duration
end_time = datetime.datetime.now() + datetime.timedelta(minutes=number)

# MAIN:
try:
    with open(output_file, "a") as f:
        up_dog = 0  # Go ahead, ask me what it is.
        while datetime.datetime.now() < end_time:
            # For the specified number of loops, do the following:
            # Ping, -c is count, hostname is the target, dev null sends terminal output to the abyss
            response = os.system(f"ping -c 1 {hostname} > /dev/null 2>&1")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if response == 0:  # If there's a positive response, add one to up_dog.
                #what's
                up_dog += 1  # Nothing much, dog. What's up with you?
                status = "UP"
            else:
                status = "DOWN"
            result = f"{timestamp}, {hostname}, {status}"
            # print(result)  # Printing result to the terminal (commented out for real-world use)
            f.write(result)  # Writing result to the file
            time.sleep(2)  # Wait 2 seconds before looping
except Exception as e:
    print(f"An error occurred: {e}")
