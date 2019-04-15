# ********************************************************************************
# *File Name:- Get_CPU_Count.py
# *Service Name:-
# *Purpose: To Validate input parameters with their types
# *Author Name: Akhil kumar
# *Create Date: 9 April 2019
# *Modify By:-
# *Last Modify Date:
# *Current Version: 1.0
# *Summary of Last Change:
# *****
import sys
import psutil
import logging
from math import ceil
sys.path.insert(0, '../LIb/')
sys.path.insert(0, '../Variables/')
from Validate_Input import *
from Global import *
# print Log_Level
# LogFile='C:\\Users\\akhil-k\\Moogsoft_PreRequisites\\Log\\getcpu.log'
def Fun_Get_CPU_Count(tocheck,LogFile):
	logging.basicConfig(filename=LogFile, 
                    format='%(asctime)s %(message)s', 
                    filemode='a') 
  
	#Creating an object 
	logger=logging.getLogger() 
	  
	#Setting the threshold of logger to DEBUG 
	logger.setLevel(logging.INFO)
	logger.info('Input Arguments are %s %s', tocheck,LogFile)
	if Log_Level==2:
		logger.info('Converting memory in bytes to GB')
	Cpu_Count = psutil.cpu_count()
	if Log_Level==2:
		logger.info('Comparing total memory with recommended memory')
	if Cpu_Count < tocheck:
		if Log_Level==2:
			logger.info('No. of CPUs is less than the recommended value')
		logger.info('Exiting Fun_Get_CPU_Count with False value')
		return False
	else:
		if Log_Level==2:
			logger.info('CPU Count is more than or equal to the recommended value')
		logger.info('Exiting Fun_Get_CPU_Count with True value')
		return True
	
# st=Fun_Get_CPU_Count(11,LogFile)
# print st