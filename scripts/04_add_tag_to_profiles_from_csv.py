'''
Created on Jun 20, 2017

@author: Vinh
'''
import settings        
import json
import requests
import csv

if __name__ == '__main__':
    #===========================================================================
    # Define variables
    #===========================================================================
    addTagToProfileAPIUrl = "https://api.multiloginapp.com/v1/tag/profile/add?token=%s&tagId=%s&profileId=%s"
    importCSVPath = "files/input/add_tag_to_profiles.csv"
    dictIndexName = {'profileId': 0,'tagId': 1, 'token': 2}
    
    #===========================================================================
    # Get information from CSV file
    #===========================================================================
    # For each record in csv file
    with open(importCSVPath, 'rb') as inp:
        firstline = True
        for row in csv.reader(inp):
            if firstline:    # Skip first line
                firstline = False
                continue
            
            #===================================================================
            # Get data from csv file and assign to variables
            #===================================================================
            tagId =  row[dictIndexName.get("tagId")]
            profileId =  row[dictIndexName.get("profileId")]
            token =  row[dictIndexName.get("token")]
            
            #===================================================================
            # Assign value to body data   
            #===================================================================
            payload =   {}
            
            #===================================================================
            # Post data to API
            #===================================================================
            json_encoded_payload = json.dumps(payload)
            headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
            response = requests.get(addTagToProfileAPIUrl % (token, tagId, profileId), data=json_encoded_payload, headers=headers)
            
            #===================================================================
            # Report
            #===================================================================
            if (response.status_code == 200):    
                print "Add tag to profile successful!. Profile ID = %s | Tag ID = %s" % (profileId, tagId)
            else:
                print("Cannot add tag to profile. Error Message: %s" % json.loads(response.text)["value"])

    
