#2. Write a python script which will display system name ,node name and release details of current system.
#display node
import os
os.uname().nodename
import platform
platform.node()
platform.system()
platform.release()
platform.version()
import socket
socket.gethostname()
