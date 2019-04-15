import sys
import logging
import os
sys.path.insert(0, '../LIb/')
sys.path.insert(0, '../Variables/')
from Validate_Input import *
from Global import *
Current_Location=os.path.dirname(os.path.realpath(__file__))
Location_Array=Current_Location.split('\\')
Location_Array.pop()
LogFile='\\'.join(Location_Array)
LogFile+='\Log\Logs.log'
# print(LogFile)
#Create and configure logger 
logging.basicConfig(filename=LogFile, 
                    format='%(asctime)s %(message)s', 
                    filemode='a') 
  
#Creating an object 
logger=logging.getLogger() 
  
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.INFO) 
logger.info('--------Starting-------')
logger.info("Log Level set to %s", Log_Level) 
logger.info("Calling Function Fun_Validate_input") 
st=Fun_Validate_Input(sys.argv,['char','int'],LogFile)
logger.info('--------Exit-----------')
print(st)