import requests
import time
import lxml
import sys
import os
import twitter_piracy
from lxml import etree

TWITTER_USERNAME = os.environ["TWITTER_USERNAME"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
TWITTER_PHONE_NUMBER = os.environ["TWITTER_PHONE_NUMBER"]

UPDATELIST_XML_URL = "http://fus01.ps5.update.playstation.net/update/ps5/official/tJMRE80IbXnE9YuG0jzTXgKEjIMoabr6/list/us/updatelist.xml"    

def getLastPup():
    return open("lastpup.txt","r").read()

def setLastPup(lastPup):
    return open("lastpup.txt","w").write(lastPup)

def getLastVersion():
    return open("lastversion.txt","r").read()

def setLastVersion(lastVer):
    return open("lastversion.txt","w").write(lastVer)

def savepagenow(url):
    try:
        requests.post("https://web.archive.org/save/"+url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}, data={"url":url, "capture_all": "on"})
    except:
        pass

def checkForUpdate():
    print("Checking for update....")
    xmlRequest = requests.get(UPDATELIST_XML_URL, headers={"Cache-Control": "no-cache","User-Agent":"PS5 Update Checker by SilicaAndPina!"})
    xmlData = lxml.etree.fromstring(xmlRequest.text)
    systemPup = xmlData.xpath('/update_data_list/region/system_pup')[0]
    updateVersion = systemPup.get('label')
    pupFile = xmlData.xpath("/update_data_list/region/system_pup/update_data/image")[0].text
    
    lastPup = getLastPup()
    lastVersion = getLastVersion()
    
    if pupFile != lastPup:
        text = ""
        if lastVersion == updateVersion:
            text = "Sony just stealth 1000 pushed PS5 Update "+updateVersion+"\nOld PUP: "+lastPup+"\nNew PUP: "+pupFile+"\n@Darthsternie @LiEnbyy #PS5UpdateChecker #TransRightsAreHumanRights"
        else:
            text = "Sony just pushed PS5 Update "+updateVersion+"!\nPUP: "+pupFile+"\nPrevious version was "+lastVersion+"\n@Darthsternie @LiEnbyy #PS5UpdateChecker #TransRightsAreHumanRights"
        
        print(text)
        
        twitter_piracy.login(TWITTER_USERNAME, TWITTER_PASSWORD, TWITTER_PHONE_NUMBER)
        twitter_piracy.tweet(text)
        
        setLastPup(pupFile)
        setLastVersion(updateVersion)
        
        print("Sending to wayback machine.")
        
        savepagenow(UPDATELIST_XML_URL)
        savepagenow(pupFile)
        
    else:
        print("No update found....")
        
checkForUpdate()