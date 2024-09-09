import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
from urllib.request import urlopen
import os
import sys
from os import path
import random
import pickle
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from tabulate import tabulate
from parinya import LINE

def farm_feed():

    #! Get full path program.
    Fullpath = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))
    
    UnCodeKey = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "@"]
    
    #! input
    input_start_account = int(input("start account : "))
    input_end_account = int(input("end account : "))
    url = "https://mobile.facebook.com"
    
    #! random profile
    sum_ran_p = (input_end_account-input_start_account)+1
    ran_prof = random.sample(range(input_start_account, (input_end_account+1)), sum_ran_p)
    # print("ran_prof = ", ran_prof)
    
    #!count 
    num_openprofile = 0
    get_uid = ""
    datatable = []
    
   #! loop from number profile
    for i in range(0 ,sum_ran_p):
    
        #! select profile
        profile = ran_prof[i]
        print(f"--profile used = {profile}--")
        num_openprofile += 1
    
        #! get uid
        try:
            cookie_uid = pickle.load(open(f"{Fullpath}\\cookie\\cookies{profile}.pkl", "rb"))
            cookie_str = (str(cookie_uid))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    get_uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", ""))
                    break    
        except:
            print("--get uid ERR--")
            
        #! read chrome file 
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome{profile}", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"
    
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome{profile}", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()
        #! open browser
        opt1 = Options()
        opt1.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt1.add_argument(f'--profile-directory={strings}')
        opt1.add_argument("--start-maximized")
        opt1.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt1.add_argument("--disable-notifications")
        opt1.add_argument("--disable-infobars")
        opt1.add_argument("--window-position=0,0")
        opt1.add_argument("--window-size=360,900")
        opt1.add_experimental_option('excludeSwitches', ['enable-logging'])
        # opt1.add_argument('--headless')
        driver1 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt1)
        driver1.get(url)
        #! add cookie
        try:
            driver1.delete_all_cookies()
            cookies1 = pickle.load(open(f"{Fullpath}\\cookie\\cookies{profile}.pkl", "rb"))
            for cookie1 in cookies1:
                driver1.add_cookie(cookie1)
            driver1.refresh()
            time.sleep(random.uniform(4, 10))
        except:
            print(f"--profile {profile} Not add cookie--")
            print("=======================================================================")
            driver1.quit()
            continue
        
        
        #! check like
        try:
            driver1.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
        except:
            add_table_profile_ck = [profile ,get_uid ,"" ,"" ,"check point"]
            datatable.append(add_table_profile_ck)
            print(f"--profile {profile} check point--")
            print("=======================================================================")
            driver1.quit()
            continue
        
        
        #! random read_notifi
        read_notifi = random.randint(2, 4)
        
        
        #print
        print("read_notifi = ", read_notifi)

        #! click notifi
        
        try:
            notifi_tab = driver1.find_element(by=By.XPATH, value="//div[@id='notifications_jewel']")
            notifi_tab.click()
            time.sleep(random.uniform(3, 5))
        except:
            print("error click notifi tab")
            driver1.quit()
            continue
        
        for read in range(0, read_notifi):
            try:
                notifi = driver1.find_elements(by=By.XPATH, value="//div[@data-sigil='notification marea']")
                driver1.execute_script("arguments[0].scrollIntoView(true);", notifi[read])
                driver1.execute_script("window.scrollBy(0, -200)")
                time.sleep(0.50)
                notifi[read].click()
            except:
                print("error scroll and click")
            time.sleep(random.uniform(5, 10))
            driver1.back()
            time.sleep(random.uniform(1, 2))
            
        time.sleep(random.uniform(5, 12))
        driver1.quit()
        
farm_feed()