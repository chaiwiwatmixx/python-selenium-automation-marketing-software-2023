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

def check_group():

    #! Get full path program.
    Fullpath = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))
    #print(Fullpath)
    
    UnCodeKey = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "@"]
    
    #! input
    input_start_account = int(input("start account : "))
    input_end_account = int(input("end account : "))
    url = "https://mobile.facebook.com/groups/"
    print("<<=======================================================================>>")
    
    #!read  uid
    group_id_txt = open(f"{Fullpath}\\real_use\\check_group\\group_id.txt", "r" ,encoding='utf-8')
    group_id = ""
    group_id = group_id_txt.read().split("\n")
    group_id_txt.close()

    #! read line key
    filetxt_line_key = open("line_key.txt", "r",encoding='utf-8')
    line_key = ""
    line_key = filetxt_line_key.read()
    filetxt_line_key.close()
    input_line_key = line_key
    line = LINE(input_line_key)
    #! select stiker
    list_await = [[1, 103], [1, 1], [1, 402], [1, 404], [1, 404], [1, 424], [1, 430], [2, 140], [2, 155], [2, 502], [2, 503], [2, 513], [2, 512], [2, 524]]
    list_complat = [[1, 106], [1, 116], [1, 41], [1, 413], [2, 28], [2, 40], [2, 41], [2, 45], [2, 147], [2, 527]]
    random_await = (random.choice(list_await))
    random_complat = (random.choice(list_complat))
    #! line before notify
    try:
        line.sendtext(f"กำลังดำเนินการเช็คกลุ่มทั้งหมด {len(group_id)} กลุ่ม  กรุณารอสักครู่")
        line.sendsticker(random_await[0], random_await[1])
    except:
        print("--ERROR line before notify--")
        print("-----------------------------------------------------------------------")
    
    #! random profile
    sum_ran_p = (input_end_account-input_start_account)+1
    ran_prof = random.sample(range(input_start_account, (input_end_account+1)), sum_ran_p)
    # print("ran_prof = ", ran_prof)
    
    #!count 
    num_groupid_use = 0
    num_can_comment = 0
    num_cannot_comment = 0
    groupuid_remain = len(group_id)
    num_openprofile = 0
    get_uid = ""
    remove_groupid = []
    datatable = []
    CP = []
    
    #! loop from number profile
    for i in range(0 ,len(group_id)-1):
        
        #! check remain
        if groupuid_remain == 0:
            break

        #! select profile
        profile = 0
        while True:
            ran_profile = random.randint(input_start_account, input_end_account)
            if ran_profile in CP:
                pass
            else:
                profile = ran_profile
                break
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
            print("ERR get uid")    
        
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
        opt1.add_argument("--window-size=360,740")
        opt1.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt1.add_argument('--headless')
        driver1 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt1)
        driver1.get("https://mobile.facebook.com")
        
        #! check load
        for l_ck in range(0, 14):
            try:
                driver1.find_element(by=By.XPATH, value="//button[@name='login']")
                break
            except:
                try:
                    driver1.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                    break
                except:
                    time.sleep(0.5)
        
        #! add cookie
        try:
            driver1.delete_all_cookies()
            cookies1 = pickle.load(open(f"{Fullpath}\\cookie\\cookies{profile}.pkl", "rb"))
            for cookie1 in cookies1:
                driver1.add_cookie(cookie1)
            driver1.refresh()
        except:
            print(f"--profile {profile} Not add cookie--")
            print("=======================================================================")
            driver1.quit()
            continue
        
        #! check load
        for l_ck in range(0, 14):
            try:
                driver1.find_element(by=By.XPATH, value="//button[@name='login']")
                break
            except:
                try:
                    driver1.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                    break
                except:
                    time.sleep(0.5)
        

        #! check like
        try:
            driver1.find_element(by=By.XPATH, value="//i[@id='MBackNavBarLeftArrow']")
        except:
            CP.append(profile)
            add_table_profile_ck = [profile ,"" ,"" ,"check point"]
            datatable.append(add_table_profile_ck)
            print(f"--profile {profile} check point--")
            print("=======================================================================")
            driver1.quit()
            continue
        time.sleep(1)
        
        #! count
        CP_comment = False
        num_check = random.randint(5, 10)
        # print("num_check = ", num_check)
        print("-----------------------------------------------------------------------")
        print
        
        for l in range(0, num_check):
            
            #! open group
            try:
                driver1.get(url+group_id[num_groupid_use])
            except:
                print("--Not open group--")
                
            #! check load
            for l_cl in range(0, 18):
                try:
                    driver1.find_element(by=By.XPATH, value="//div[contains(text(),'Write something...')]")
                    break
                except:
                    time.sleep(0.5)
                    
            #! check like
            try:
                driver1.find_element(by=By.XPATH, value="//i[@id='MBackNavBarLeftArrow']")
                groupuid_remain -= 1
            except:
                CP.append(profile)
                add_table_profile_ck = [profile ,"" ,"" ,"check point"]
                datatable.append(add_table_profile_ck)
                print(f"--profile {profile} check point--")
                print("=======================================================================")
                driver1.quit()
                break
            
            #! scroll down
            driver1.execute_script("window.scrollBy(0, 1000)")
            time.sleep(random.uniform(0.1, 0.5))
            
            #! check group
            try:
                driver1.find_element(by=By.XPATH, value="//a[normalize-space()='Comment']")
                num_can_comment += 1
            except:
                try:
                    driver1.find_element(by=By.XPATH, value="//div//span[contains(text(),'Admins control who posts and comments · Request to')]")
                    num_cannot_comment += 1
                    remove_groupid.append(group_id[num_groupid_use])
                    # group_id.remove(group_id[num_groupid_use])
                    # with open(f"{Fullpath}\\real_use\\check_group\\group_id.txt","w") as tfile:
                    #     tfile.write('\n'.join(group_id))
                except:
                    print("--error check group--")
            num_groupid_use += 1
            print("num_can_comment = ",num_can_comment)
            print("num_cannot_comment = ",num_cannot_comment)
            print("-----------------------------------------------------------------------")
            
            time.sleep(random.uniform(0.50, 6))
            
            #! check remain
            if groupuid_remain == 0:
                break
        #! close browser
        driver1.quit()
        if groupuid_remain == 0:
            print("groupuid_remain = ", groupuid_remain)
            break
    #! remove group
    try:
        for re in range(0, len(remove_groupid)):
            group_id.remove(remove_groupid[re])
            with open(f"{Fullpath}\\real_use\\check_group\\group_id.txt","w") as tfile:
                tfile.write('\n'.join(group_id))
    except:
        print("--error delete group--")
    #! line notify
    line.sendtext(f"เช็คกลุ่มสำเร็จ {num_groupid_use} กลุ่ม\n-กลุ่มที่คอมเม้นได้ {num_can_comment} กลุ่ม\n-กลุ่มที่คอมเม้นไม่ได้ {num_cannot_comment} กลุ่ม") 
    line.sendsticker(random_complat[0], random_complat[1])
    #! add data table SUM
    add_table_sum = [num_groupid_use ,num_can_comment ,num_cannot_comment ,"Complete"]
    datatable.append(add_table_sum)
    #! show data table
    col_names = ["all groups","can comment" ,"can't comment", "status"]
    print(tabulate(datatable, headers=col_names, tablefmt="fancy_grid"))
# check_group()