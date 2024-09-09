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

def farm_share_post():

    #! Get full path program.
    Fullpath = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))
    
    UnCodeKey = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "@"]
    
    #! input
    input_start_account = int(input("start account : "))
    input_end_account = int(input("end account : "))
    url = "https://mobile.facebook.com/"
    
    #! random profile
    sum_ran_p = (input_end_account-input_start_account)+1
    ran_prof = random.sample(range(input_start_account, (input_end_account+1)), sum_ran_p)
    # print("ran_prof = ", ran_prof)
    
    #!read  uid
    page_id_txt = open(f"{Fullpath}\\real_use\\fram\\share_post\\page_id.txt", "r" ,encoding='utf-8')
    page_id = ""
    page_id = page_id_txt.read().split("\n")
    page_id_txt.close()
    
    #!count 
    num_openprofile = 0
    get_uid = ""
    datatable = []
    num_pageid_use = 0
    
   #! loop from number profile
    for i in range(0 ,sum_ran_p):

        #! check number page
        if len(page_id) >= sum_ran_p:
            pass
        else:
            print("Enter page less than  number of accounts")
            print("=======================================================================")
            break
    
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
        driver1.get("https://mobile.facebook.com")
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

        #! open page
        try:
            driver1.get(url+page_id[num_pageid_use])
        except:
            print(f"--profile {profile} error open page --")
            print("=======================================================================")
            driver1.quit()
            continue
        time.sleep(random.uniform(2, 4))

        #! scroll down
        try:
            driver1.execute_script("window.scrollBy(0, 1000)")
            time.sleep(random.uniform(2, 3))
            driver1.execute_script("window.scrollBy(0, 1000)")
            time.sleep(random.uniform(0.1, 0.5))
        except:
            print(f"--profile {profile} scroll down 2000 --")
            print("=======================================================================")
            driver1.quit()
            continue

            
        #! scroll to share tab
        try:
            ran_select_share = random.randint(0, 7)
            print("ran_select_share =", ran_select_share)
            share_tab = driver1.find_elements(by=By.XPATH, value="//a[contains(text(),'Share')]")
            time.sleep(random.uniform(0.50, 1))
            driver1.execute_script("arguments[0].scrollIntoView(true);", share_tab[ran_select_share])
            share_tab[ran_select_share].click()
        except:
            try:
                time.sleep(random.uniform(2, 3))
                driver1.execute_script("window.scrollBy(0, 1000)")
                time.sleep(random.uniform(2, 3))
                driver1.execute_script("window.scrollBy(0, 1000)")
                time.sleep(random.uniform(0.1, 0.5))

                ran_select_share = random.randint(0, 7)
                print("ran_select_share =", ran_select_share)
                share_tab = driver1.find_elements(by=By.XPATH, value="//a[contains(text(),'Share')]")
                time.sleep(random.uniform(0.50, 1))
                driver1.execute_script("arguments[0].scrollIntoView(true);", share_tab[ran_select_share])
                share_tab[ran_select_share].click()
            except:
                print(f"--profile {profile} error scroll to share tab --")
                print("=======================================================================")
                driver1.quit()
                continue
        time.sleep(random.uniform(3, 4))

        # #! click share
        try:
            driver1.find_element(by=By.XPATH, value="//a[@id='share-one-click-button']").click()
            num_pageid_use += 1
            time.sleep(random.uniform(15, 20))
        except:
            try:
                driver1.find_element(by=By.XPATH, value="//button[@id='share_submit']").click()
                num_pageid_use += 1
                time.sleep(random.uniform(15, 20))
            except:
                print(f"--profile {profile} error click share--")
                print("=======================================================================")
                driver1.quit()
                continue
        driver1.quit()
        time.sleep(random.uniform(5, 8))
        
        
farm_share_post()