'''
Created on Jun 20, 2017

@author: Vinh
'''
import settings
import libs

if __name__ == '__main__':
    
        
    #===========================================================================
    # Define variables
    #===========================================================================
    listUrl = "https://api.multiloginapp.com/v1/profile/list?token=8c7c251554b4fb5f72c9b01e486a3e0d49d132a7"
    detailUrl = "https://api.multiloginapp.com/v1/profile/get-data?profileId=%s&token=8c7c251554b4fb5f72c9b01e486a3e0d49d132a7"
    resultPath = "files/output/" # REMEMBER TO ADD "/" AT THE END OF PATH
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
    
    # Pause the script at the end
    print "#==========================================================================="
    print "# Finished running the script. Press enter to close..."
    print "#==========================================================================="
    raw_input()
