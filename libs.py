'''
Created on Jun 20, 2017

@author: Vinh
'''
import csv
import datetime
import json
import os
from time import strftime, gmtime
import time

import requests


def getJsonDataFromAPI(url):
    response = requests.request("GET", url)
    jsonData = json.loads(response.text)
    return jsonData

def createReportFolder(reportPath):
    # Create report path
    d = os.path.dirname(reportPath)
    if not os.path.exists(d):
        os.makedirs(d)

def killExcelFileProcess(path):
    for i in range(1,4):
        try:
            if (os.path.isfile(path)):
                open(path, "r+") # or "a+", whatever you need
            return
        except IOError:
            print "The Record file is OPENED! Please close this file now! All excel files will be KILLED after 3 mins if the Report file isn't closed!!!!"
            time.sleep(60)
    
    try:
        os.system("taskkill /im excel.exe")
    except:
        pass

def addListDataToCSVFile(filePath, jsonData):
    killExcelFileProcess(filePath)
    
    # Delete current file if it already exist
    try:
        os.remove(filePath)
    except:
        pass
    
    # Add data to csv file
    with open(filePath, 'wb') as out:
        writer = csv.writer(out)
        writer.writerow(["sid", "name", "browserName"])
        
        for row in jsonData:
            print "SID = %s" % row["sid"]
            fields = [row["sid"], row["name"], row["browserName"]]
            writer.writerow(fields)

def addDetailDataToCSVFile(filePath, listData, detailUrl):
    killExcelFileProcess(filePath)
    
    # Delete current file if it already exist
    try:
        os.remove(filePath)
    except:
        pass
    
    # Add data to csv file
    with open(filePath, 'wb') as out:
        writer = csv.writer(out)
        writer.writerow(["name", "browserType", "proxyHost", "proxyPort", "proxyIpValidation", "proxyType", "userAgent", "disablePlugins", "disableWebrtcPlugin", "disableFlashPlugin", 
                         "useZeroFingerprints", "canvasDefType", "platform", "doNotTrack", "hardwareConcurrency", "appVersion", "buildID", "langHdr", "screenHeight", "screenWidth", 
                         "id", "shared", "canvasNoiseHash", "fonts"])
        
        for data in listData:  
            # Get json data from api link
            row = getJsonDataFromAPI(detailUrl % data["sid"])
#             print row
            
            
             
            #===================================================================
            # Handle field does not exist
            #===================================================================
            try:
                proxyIpValidation = row["proxyIpValidation"]
            except:
                proxyIpValidation = ""
            
            try:
                proxyType = row["proxyType"]
            except:
                proxyType = ""
                
            try:
                proxyHost = row["proxyHost"]
            except:
                proxyHost = ""
            
            try:
                proxyPort = row["proxyPort"]
            except:
                proxyPort = ""
            
            try:
                name = row["name"]
            except:
                name = ""
            
            try:
                buildID = row["buildID"]
            except:
                buildID = ""
            
            try:
                browserType = row["browserType"]
            except:
                browserType = ""
            
            try:
                userAgent = row["userAgent"]
            except:
                userAgent = ""
            
            try:
                disablePlugins = row["disablePlugins"]
            except:
                disablePlugins = ""
                
            try:
                disableWebrtcPlugin = row["disableWebrtcPlugin"]
            except:
                disableWebrtcPlugin = ""
                
            try:
                useZeroFingerprints = row["useZeroFingerprints"]
            except:
                useZeroFingerprints = ""
            
            try:
                canvasDefType = row["canvasDefType"]
            except:
                canvasDefType = ""
            
            try:
                platform = row["platform"]
            except:
                platform = ""
            
            try:
                doNotTrack = row["doNotTrack"]
            except:
                doNotTrack = ""
                
            try:
                hardwareConcurrency = row["hardwareConcurrency"]
            except:
                hardwareConcurrency = ""
                
            try:
                appVersion = row["appVersion"]
            except:
                appVersion = ""
                
            try:
                langHdr = row["langHdr"]
            except:
                langHdr = ""
                
            try:
                screenHeight = row["screenHeight"]
            except:
                screenHeight = ""
                
            try:
                screenWidth = row["screenWidth"]
            except:
                screenWidth = ""
            
            try:
                disableFlashPlugin = row["disableFlashPlugin"]
            except:
                disableFlashPlugin = ""
            
            try:
                ids = row["id"]
            except:
                ids = ""
            
            try:
                shared = row["shared"]
            except:
                shared = ""
            
            try:
                canvasNoiseHash = row["canvasNoiseHash"]
            except:
                canvasNoiseHash = ""
            
            try:
                fonts = row["fonts"]
            except:
                fonts = "" 
                
            print "===================="
            print "Name = %s" % name
            print "build ID = %s" % buildID
            
            #===================================================================
            # Add fields
            #===================================================================
            fields = [name, browserType, proxyHost, proxyPort, proxyIpValidation, proxyType , userAgent, 
                    disablePlugins, disableWebrtcPlugin, disableFlashPlugin, useZeroFingerprints, canvasDefType, platform, doNotTrack, hardwareConcurrency,
                    appVersion, buildID, langHdr, screenHeight, screenWidth, ids, shared, canvasNoiseHash, fonts]
             
            writer.writerow(fields)
            
def generateUniqueValue():
    return datetime.datetime.now().strftime("%Y%m%d")