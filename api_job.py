'''
Created on Jun 20, 2017

@author: Vinh
'''
import imp
import os

def doesLibIsImported(libName):
    try:
        imp.find_module(libName)
        return True
    except ImportError:
        return False
    
if doesLibIsImported("requests") == False:
    if os.name == "nt": # Windows OS
        os.system("python -m pip install -U requests") # Install requests
        
import libs

if __name__ == '__main__':
    
        
    #===========================================================================
    # Define variables
    #===========================================================================
    listUrl = "https://api.multiloginapp.com/v1/profile/list?token=8c7c251554b4fb5f72c9b01e486a3e0d49d132a7"
    detailUrl = "https://api.multiloginapp.com/v1/profile/get-data?profileId=%s&token=8c7c251554b4fb5f72c9b01e486a3e0d49d132a7"
    resultPath = "D:/OneTenMediaGroup/results/"
    fileListName = "list_%s.csv" % libs.generateUniqueValue()
    fileDetailName = "detail_%s.csv" % libs.generateUniqueValue()
    fileListPath = resultPath + fileListName
    fileDetailPath = resultPath + fileDetailName
    
    #===========================================================================
    # Steps to get the list information 
    #===========================================================================
    # Create the result path
    libs.createReportFolder(resultPath)
    
    # Get json data from api link
    jsonData = libs.getJsonDataFromAPI(listUrl)
    
    # Save data into a csv file
    libs.addListDataToCSVFile(fileListPath, jsonData["data"])
    
    #===========================================================================
    # Steps to get the detail information 
    #===========================================================================
    # Save detail data into a csv file
    libs.addDetailDataToCSVFile(fileDetailPath, jsonData["data"], detailUrl)
