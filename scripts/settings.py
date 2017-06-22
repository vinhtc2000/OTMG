'''
Created on Jun 22, 2017

@author: Vinh
'''
import imp
import os

#===============================================================================
# Define variables
#===============================================================================


#===============================================================================
# Import libraries
#===============================================================================
def doesLibIsImported(libName):
    try:
        imp.find_module(libName)
        return True
    except ImportError:
        return False
    
if doesLibIsImported("requests") == False:
    if os.name == "nt": # Windows OS
        os.system("python -m pip install -U requests") # Install requests