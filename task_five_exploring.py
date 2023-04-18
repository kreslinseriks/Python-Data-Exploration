import re
import socket

# Get URL from user and extract hostname
try:
    url = input("Please enter the link to the web page: ")
    hostname = str(re.findall('://([\w\-\.]+)', url))
    hostname = hostname[2:len(hostname) - 2]
    url = "GET "+url+" HTTP/1.0\r\n\r\n"
except:
    print("Error.")

# Send GET request to the specific URL using the specific hostname
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((hostname, 80))
cmd = url.encode() 
mysock.send(cmd)

# Print the contents of webpage, break when 1800 characters have been reached
output = ''
while True:
    if (len(output) > 1800):
        break
    data = mysock.recv(20)
    if (len(data) < 1):
        break
    print(data.decode(),end='')
    output += str(data.decode())
mysock.close()



