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
    createProfileAPIUrl = "https://api.multiloginapp.com/v1/profile/create?token=%s"
    importCSVPath = "files/input/create_profiles.csv"
    dictIndexName = {
                        'name':0, 'browserType': 1 ,'proxyHost':2 ,'proxyPort':3 ,'proxyUser':4 ,'proxyPass':5 ,'proxyIpValidation':6 ,'proxyType':7 ,'notes':8 ,'userAgent': 9 ,
                        'disablePlugins': 10 ,'disableWebrtcPlugin': 11 ,'disableFlashPlugin': 12 ,'customExtensionFileNames': 13 ,'useZeroFingerprints': 14 ,
                        'generateZeroFingerprintsData': 15 ,'canvasDefType': 16 ,'platform': 17 ,'doNotTrack':18 ,'hardwareConcurrency': 19 ,'langHdr': 20 ,
                        'screenHeight': 21 ,'screenWidth':22 ,'timeZone':23 ,'tag':24, 'token': 25
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
            browserType =  row[dictIndexName.get("browserType")]
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
            generateZeroFingerprintsData =  row[dictIndexName.get("generateZeroFingerprintsData")]
            canvasDefType =  row[dictIndexName.get("canvasDefType")]
            platform =  row[dictIndexName.get("platform")]
            doNotTrack =  row[dictIndexName.get("doNotTrack")]
            hardwareConcurrency =  row[dictIndexName.get("hardwareConcurrency")]
            langHdr =  row[dictIndexName.get("langHdr")]
            screenHeight =  row[dictIndexName.get("screenHeight")]
            screenWidth =  row[dictIndexName.get("screenWidth")]
            timeZone =  row[dictIndexName.get("timeZone")]
            tag =  row[dictIndexName.get("tag")]
            token =  row[dictIndexName.get("token")]
            
            #===================================================================
            # Handle special variables (Not a string value)
            #===================================================================
            
            proxyIpValidation = True if (str(proxyIpValidation).upper() == "TRUE") else False
            
            disablePlugins = True if (str(disablePlugins).upper() == "TRUE") else False
            
            disableWebrtcPlugin = True if (str(disableWebrtcPlugin).upper() == "TRUE") else False
            
            disableFlashPlugin = True if (str(disableFlashPlugin).upper() == "TRUE") else False
            
            useZeroFingerprints = True if (str(useZeroFingerprints).upper() == "TRUE") else False
            
            hardwareConcurrency = int(hardwareConcurrency)
            
            #===================================================================
            # Assign value to body data   
            #===================================================================
            payload = { 
                        "name": name, # mandatory 
                        "browserType": browserType, # firefox, chrome, opera, stealth_fox # mandatory 
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
                        "generateZeroFingerprintsData": generateZeroFingerprintsData, # if you want MLA to generate zero fingerprints data automatically
                        "canvasDefType": canvasDefType, #  noise, block 
                        "platform": platform, 
                        "doNotTrack": doNotTrack, 
                        "hardwareConcurrency": hardwareConcurrency, 
                        "langHdr": langHdr, 
                        "screenHeight": screenHeight, 
                        "screenWidth": screenWidth, 
                        "timeZone": timeZone, 
                        "tag": tag
                    } 
            
            #===================================================================
            # Post data to API
            #===================================================================
            json_encoded_payload = json.dumps(payload)
            headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
            response = requests.post(createProfileAPIUrl % token, data=json_encoded_payload, headers=headers)
            
            #===================================================================
            # Report
            #===================================================================
            if (response.status_code == 200):    
                print "Add new profile successful!. ID = %s" % json.loads(response.text)["value"]
            else:
                print("Cannot add new profile. Error Message: %s" % json.loads(response.text)["value"])

    # Pause the script at the end
    raw_input()
