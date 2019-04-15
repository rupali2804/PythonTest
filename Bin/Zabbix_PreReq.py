import argparse
import sys
import logging
import os
sys.path.insert(0, '../Lib/')
sys.path.insert(0, '../Variables/')
from Validate_Input import *
# from Global import *
Current_Location=os.path.dirname(os.path.realpath(__file__))
Location_Array=Current_Location.split('\\')
Location_Array.pop()
LogFile1='\\'.join(Location_Array)
LogFile=LogFile1+'\\Log\zabbix_prereq.log'
StatusFile=LogFile1+'\\Log\\Status.log'
from Disk_Check import *
from Get_Memory import *
from Get_CPU_Count import *
Log_Level=1

logging.basicConfig(filename=LogFile, 
                    format='%(asctime)s %(message)s', 
                    filemode='a') 
  
#Creating an object 
logger=logging.getLogger() 
  
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.INFO) 
logger.info('--------Starting-------')
logger.info("Log Level set to %s", Log_Level) 
# parser = argparse.ArgumentParser()
# parser.add_argument('--Recommended_Cpu_count')
# parser.add_argument('--Recommended_Disk_Space')
# parser.add_argument('--DriveName')
# parser.add_argument('--Recommended_Memory')
# args = parser.parse_args()
# args = parser.parse_args() 
f=open(StatusFile,"w")
logger.info("Calling Function Fun_Get_CPU_Count")
Cpu_count = Fun_Get_CPU_Count(3,LogFile)
if Cpu_count[0]==False:
	f.write('Check_CPU_Count: Fail ')
	f.write(" Recommended Value is " +str(Cpu_count[2])+" , Actual Value is " + str(Cpu_count[1]) + "\n" )
elif Cpu_count[0]==True:
	f.write('Check_CPU_Count: Pass ')
	f.write("Recommended Value is " +str(Cpu_count[2])+" , Actual Value is "+ str(Cpu_count[1])+"\n" )
logger.info('Status from Fun_Get_CPU_Count is %s',Cpu_count)
logger.info("Calling Function Fun_Get_Memory")
Mem = Fun_Get_Memory(8,LogFile)
if Mem[0]==False:
	f.write('Check_Memory: Fail ')
	f.write("Recommended Value is " +str(Mem[2])+" , Actual Value is "+ str(Mem[1])+"\n" )
elif Mem[0]==True:
	f.write('Check_Memory: Pass ')
	f.write("Recommended Value is "+str(Mem[2])+" , Actual Value is "+ str(Mem[1])+"\n" )
logger.info('Status from Fun_Get_Memory is %s',Mem)
logger.info("Calling Function Fun_GetFreeDisk")
Storage=Fun_GetFreeDisk("C:",100)
if Storage[1]==1:
	f.write('Check_Disk_Space: Fail ')
	if Storage[0]=='DNF':
		f.write('Directory '+args.DriveName+ ' Not found'+"\n")
	else:
		f.write("Recommended Value is 100 , Actual Value is "+args(Storage[0])+"\n" )
elif Storage[1]==0:
	f.write('Check_Disk_Space: Pass ')
	f.write("Recommended Value is 100 Actual Value is "+str(Storage[0])+"\n" )
logger.info('Status from Fun_GetFreeDisk is %s',Storage)
logger.info('Storage')
f.close()
# print Storage
