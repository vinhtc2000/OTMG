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
    updateProfileAPIUrl = "https://api.multiloginapp.com/v1/profile/update?profileId=%s&token=%s"
    importCSVPath = "files/input/update_profiles.csv"
    dictIndexName = {
                        'name': 0,'proxyHost': 1,'proxyPort': 2,'proxyUser': 3,'proxyPass': 4,'proxyIpValidation': 5,'proxyType': 6,'notes': 7,
                        'userAgent': 8,'disablePlugins': 9,'disableWebrtcPlugin': 10,'disableFlashPlugin': 11,'customExtensionFileNames': 12,
                        'useZeroFingerprints': 13,'canvasDefType': 14,'generateNewCanvasNoise': 15,'generateNewFonts': 16,'platform': 17,'doNotTrack': 18,
                        'hardwareConcurrency': 19,'langHdr': 20,'screenHeight': 21,'screenWidth': 22,'timeZone': 23,'id': 24, 'token': 25   

                     }
    
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
            name =  row[dictIndexName.get("name")]
            proxyHost =  row[dictIndexName.get("proxyHost")]
            proxyPort =  row[dictIndexName.get("proxyPort")]
            proxyUser =  row[dictIndexName.get("proxyUser")]
            proxyPass =  row[dictIndexName.get("proxyPass")]
            proxyIpValidation =  row[dictIndexName.get("proxyIpValidation")]
            proxyType =  row[dictIndexName.get("proxyType")]
            notes =  row[dictIndexName.get("notes")]
            userAgent =  row[dictIndexName.get("userAgent")]
            disablePlugins =  row[dictIndexName.get("disablePlugins")]
            disableWebrtcPlugin =  row[dictIndexName.get("disableWebrtcPlugin")]
            disableFlashPlugin =  row[dictIndexName.get("disableFlashPlugin")]
            customExtensionFileNames =  row[dictIndexName.get("customExtensionFileNames")]
            useZeroFingerprints =  row[dictIndexName.get("useZeroFingerprints")]
            canvasDefType =  row[dictIndexName.get("canvasDefType")]
            generateNewCanvasNoise =  row[dictIndexName.get("generateNewCanvasNoise")]
            generateNewFonts =  row[dictIndexName.get("generateNewFonts")]
            platform =  row[dictIndexName.get("platform")]
            doNotTrack =  row[dictIndexName.get("doNotTrack")]
            hardwareConcurrency =  row[dictIndexName.get("hardwareConcurrency")]
            langHdr =  row[dictIndexName.get("langHdr")]
            screenHeight =  row[dictIndexName.get("screenHeight")]
            screenWidth =  row[dictIndexName.get("screenWidth")]
            timeZone =  row[dictIndexName.get("timeZone")]
            id =  row[dictIndexName.get("id")]
            token =  row[dictIndexName.get("token")]
            
            #===================================================================
            # Handle special variables (Not a string value)
            #===================================================================
            
            proxyIpValidation = True if (str(proxyIpValidation).upper() == "TRUE") else False
            
            disablePlugins = True if (str(disablePlugins).upper() == "TRUE") else False
            
            disableWebrtcPlugin = True if (str(disableWebrtcPlugin).upper() == "TRUE") else False
            
            disableFlashPlugin = True if (str(disableFlashPlugin).upper() == "TRUE") else False
            
            useZeroFingerprints = True if (str(useZeroFingerprints).upper() == "TRUE") else False
            
            generateNewCanvasNoise = True if (str(generateNewCanvasNoise).upper() == "TRUE") else False
            
            generateNewFonts = True if (str(generateNewFonts).upper() == "TRUE") else False
            
            hardwareConcurrency = int(hardwareConcurrency)
            
            #===================================================================
            # Assign value to body data   
            #===================================================================
            payload =   {
                            "name": name,
                            "proxyHost": proxyHost, 
                            "proxyPort": proxyPort, 
                            "proxyUser": proxyUser, 
                            "proxyPass": proxyPass, 
                            "proxyIpValidation": proxyIpValidation, 
                            "proxyType": proxyType, # http, socks4, socks5 
                            "notes": notes, 
                            "userAgent": userAgent, 
                            "disablePlugins": disablePlugins, 
                            "disableWebrtcPlugin": disableWebrtcPlugin, 
                            "disableFlashPlugin": disableFlashPlugin, 
                            "customExtensionFileNames": customExtensionFileNames, 
                            "useZeroFingerprints": useZeroFingerprints, 
                            "canvasDefType": canvasDefType, # noise, block 
                            "generateNewCanvasNoise": generateNewCanvasNoise, #generate a new noise after the update
                            "generateNewFonts": generateNewFonts, #use new fonts after the update
                            "platform": platform, 
                            "doNotTrack": doNotTrack, 
                            "hardwareConcurrency": hardwareConcurrency, 
                            "langHdr": langHdr, 
                            "screenHeight": screenHeight, 
                            "screenWidth": screenWidth, 
                            "timeZone": timeZone  
                        }
            
            #===================================================================
            # Post data to API
            #===================================================================
            json_encoded_payload = json.dumps(payload)
            headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
            response = requests.post(updateProfileAPIUrl % (id, token), data=json_encoded_payload, headers=headers)
            
            #===================================================================
            # Report
            #===================================================================
            if (response.status_code == 200):    
                print "Update profile successful!. ID = %s" % json.loads(response.text)["value"]
            else:
                print "Profile ID = %s" % (id)
                print "Token = %s" % token
                print("Cannot update profile. Error Message: %s" % json.loads(response.text)["value"])

    # Pause the script at the end
    print "#==========================================================================="
    print "# Finished running the script. Press enter to close..."
    print "#==========================================================================="
    raw_input()
