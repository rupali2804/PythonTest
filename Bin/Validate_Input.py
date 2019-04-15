# ********************************************************************************
# *File Name:- Validate_Input.py
# *Service Name:-
# *Purpose: To Validate input parameters with their types
# *Author Name: Akhil kumar
# *Create Date: 5 April 2019
# *Modify By:-
# *Last Modify Date:
# *Current Version: 1.0
# *Summary of Last Change:
# ********************************************************************************

import sys
import logging
Log_Level=1
sys.path.insert(0, '../Variables/')
# from Global import *
def Fun_Validate_Input(Arg_List,Type_List,LogFile):
	#Create and configure logger 
	logging.basicConfig(filename=LogFile, 
						format='%(asctime)s %(message)s', 
						filemode='a') 
  
	#Creating an object 
	logger=logging.getLogger() 
	#Setting the threshold of logger to INFO 
	logger.setLevel(logging.INFO) 
	logger.info('Input Arguments are %s %s %s', Arg_List,Type_List,LogFile)
	# Arg_List = Arg_List.replace('[','')
	# Arg_List = Arg_List.replace(']','')
	# List1 = Arg_List.split(',')
	# Type_List = Type_List.replace('[','')
	# Type_List = Type_List.replace(']','')
	# List2 = Type_List.split(',')
	List1=Arg_List
	List1.pop(0)
	List2=Type_List
	if Log_Level==2:
		logger.info('Checking Length of Input List for length validation')
	if(len(List1) != len(List2)):
		logger.info('Length of Input lists is not same. Kindly Check!!')
		logger.info('Exiting Fun_Validate_Input with False')
		return False
	else:
		if Log_Level==2:
			logger.info('Length of Input lists is verified. Now checking for type validation')
		for i in range(0,len(List1)):
			List1[i] = List1[i].replace('\'','')
			List1[i] = List1[i].replace('\"','')
			List1[i]=List1[i].strip()
			Elem=List1[i]
			if List2[i]=='int' and Elem.isdigit():
				continue
			elif List2[i]=='char' and Elem.isalpha():
				continue
			else:
				if Log_Level==2:
					logger.info('%s does not match with type %s', Elem,List2[i])
				logger.info('Exiting Fun_Validate_Input with False')
				return False
		else:
			logger.info('Exiting Fun_Validate_Input with True')
			return True
			
				
				
	
	
