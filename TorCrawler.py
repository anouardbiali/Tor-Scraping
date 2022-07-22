import random 
import numpy as np
from stem import Signal
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os
import time 
from fake_useragent import UserAgent

useragent = UserAgent()

def switchIP():
    #Channel Traffic from specific country or countries
    #controller.set_options({'ExitNodes': '{uk},{us},{ru}'})
    with Controller.from_port(port = 9151) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
        
def getproxy(portname,portp):
    torexe = os.popen(r'c:\\Users\\user\\Desktop\\Tor Browser\\Browser\\TorBrowser\\Tor\\tor.exe')
    profile = FirefoxProfile(r'C:\\Users\\user\\Desktop\\Tor Browser\\Browser\\TorBrowser\\Data\\Browser\\profile.default')
    profile.set_preference("general.useragent.override", useragent.random)
    profile.set_preference('network.proxy.type', 1)
    profile.set_preference('network.proxy.socks', portname)
    profile.set_preference('network.proxy.socks_port',int(portp))
    profile.set_preference("network.proxy.socks_remote_dns", True)
    profile.set_preference( "javascript.enabled", False)
    profile.update_preferences()
    return webdriver.Firefox(firefox_profile= profile)
    

def main():
    clicks = random.randint(75,382)
    try:
        for i in range(clicks):
            try:
                delays = random.randint(1,45)
                delay = np.random.choice(delays)
                tmemail = random.randint(3,6)
                driver = getproxy("127.0.0.1", 9150)
                driver.get('your_website')
                time.sleep(tmemail)
                driver.find_element_by_link_text('your_link').click()
                time.sleep(tmemail)
                switchIP()
                driver.quit()
                time.sleep(delay)
            except:
                switchIP()
                driver.quit()
                time.sleep(delay)
                continue
    except:
       time.sleep(30)
       switchIP()
       driver.quit()
        
        
if __name__ == "__main__":
    main()

