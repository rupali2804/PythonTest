#File Name:- Disk_Check.py
#Service Name:- Disk size
#Purpose: To return the status of Disk Check Qualification criteria.
#Author Name: Roy Bright
#Create Date: 2/Apr/2018
#Modifed By:- Roy Bright
#Last Modify Date: 2/Apr/2019
#Current Version: 1.1
#Summary of Last Change: N/A
#Arguments: Drive/File system name and Min Size of disk required.
import socket,  ctypes, platform, os, sys, win32api

def Fun_GetFreeDisk(dirname,size):
    from Get_Platform import Fun_platform
    # print dirname
    # print size
    oss=Fun_platform(socket.gethostname())      #Calling Platform function to get OS name.
    # print ("OS is ", oss)
    #Return folder/drive free space (in megabytes).
    if oss == "Windows":                        #Enter Windows OS block
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]      #Fetch list of available drives in the server.
        # print(drives)
        flag=0
        for i in drives:                        #Check if passed drive name is present in the server.
            # i=i.replace('\\','')
            # print(i)
            if dirname not in i:
                flag = 1
            else:
                flag = 0
                break
        if flag == 0:
            free_bytes = ctypes.c_ulonglong(0)
            ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname), None, None, ctypes.pointer(free_bytes))   #Calculating Free Disk space of the Drive.
            f= round(((free_bytes.value / 1024) / 1024) /1024)
            # print(f)
            if int(f) >= int(size):
                return [f, 0]
            else:
                return [f, 1]
        else:
            # print('in lese')
            return ["DNF", 1]  #Return if Drive Not Found (DNF)
    else:                      #Enter Linux OS Block
        # print("Linux block invoked")
        import commands
        mount = commands.getoutput('ls /')  #Fetching list of File Systems on the server.
        print(mount)
        if dirname in mount:                #Check if passed FS name is present in the server
            fs = "/" + dirname
            #print(fs)
            st = os.statvfs(fs)
            ldisk = int(round((st.f_bavail * st.f_frsize / 1024 / 1024) / 1024))    #Calculating Free Disk space of the Drive.
            # print(fs, "disk size is ", ldisk, "and passed size is ", size)
            if ldisk >= size:
                return ldisk,0
            else:
                return ldisk,1
        else:
            return "DNF", 1

# disk= Fun_GetFreeDisk("C:",500)
# print disk
# if disk[1] == 0:
    # print("Disk Check Passed. Free disk space is ", int(disk[0]))
# elif disk[0] == "DNF":
    # print("File System not found in the System. ")
# else:
    # print("Disk Check Failed. Free disk space is: ", int(disk[0]))