#2. Write a python script which will display system name ,node name and release details of current system.
#display node
import os,platform,socket
os.uname().nodename
platform.node()
platform.system()
platform.release()
platform.version()
socket.gethostname()
