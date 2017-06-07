#2. Write a python script which will display system name ,node name and release details of current system.
#display node
import socket
import platform
print(socket.gethostname())
print(platform.platform())
print(platform.release())

