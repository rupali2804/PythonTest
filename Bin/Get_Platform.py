#File Name:- Get_Platform.py
#Service Name:- Platform service
#Purpose: To return the Operating System of the server
#Author Name: Roy Bright
#Create Date: 2/Apr/2018
#Modifed By:- Roy Bright
#Last Modify Date: 2/Apr/2019
#Current Version: 1.1
#Summary of Last Change: N/A
import sys
import socket
Log_Level=1
def Fun_platform(server):
    platforms = {'linux1' : 'Linux',
                 'linux2' : 'Linux',
                 'win32' : 'Windows'
                 }
    if sys.platform not in platforms:
        return sys.platform
    else :
        return platforms[sys.platform]
plat=Fun_platform(socket.gethostname())
print(plat)