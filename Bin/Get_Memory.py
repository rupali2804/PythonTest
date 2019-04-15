# ********************************************************************************
# *File Name:- Get_Memory.py
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
Log_Level=1
# from Global import *
# print Log_Level
# LogFile='C:\\Users\\akhil-k\\Moogsoft_PreRequisites\\Log\\getmem.log'
def Fun_Get_Memory(tocheck,LogFile):
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
	mem=round(psutil.virtual_memory().total/1024,3)
	# print mem
	mem=round(mem/1024,3)
	# print mem
	mem=round(mem/1024,3)
	mem=ceil(mem)
	if Log_Level==2:
		logger.info('Comparing total memory with recommended memory')
	if int(mem) < int(tocheck):
		if Log_Level==2:
			logger.info('Total memory is less than the recommended value')
		logger.info('Exiting Fun_get_memory with False value')
		return [False,mem,tocheck]
	else:
		if Log_Level==2:
			logger.info('Total memory is more than or equal to the recommended value')
		logger.info('Exiting Fun_get_memory with True value')
		return [True,mem,tocheck]
	
# st=Fun_Get_Memory(11,LogFile)
# print st