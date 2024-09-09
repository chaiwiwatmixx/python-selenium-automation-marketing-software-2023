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

def join_group():

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
    group_id_txt = open(f"{Fullpath}\\real_use\\joingroup\\group_id.txt", "r" ,encoding='utf-8')
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
        line.sendtext(f"กำลังดำเนินการนำบัญชีเข้าร่วมกลุ่ม {len(group_id)} กลุ่ม  กรุณารอสักครู่")
        line.sendsticker(random_await[0], random_await[1])
    except:
        print("--ERROR line before notify--")
        print("-----------------------------------------------------------------------")
        
    #! random profile
    sum_ran_p = (input_end_account-input_start_account)+1
    ran_prof = random.sample(range(input_start_account, (input_end_account+1)), sum_ran_p)
    # print("ran_prof = ", ran_prof)
    
    #!count 
    num_openprofile = 0
    join_group_all = 0 
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
        opt1.add_argument("--window-size=360,740")
        opt1.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt1.add_argument('--headless')
        driver1 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt1)
        driver1.get(url)
        #! add cookie
        try:
            cookies1 = pickle.load(open(f"{Fullpath}\\cookie\\cookies{profile}.pkl", "rb"))
            for cookie1 in cookies1:
                driver1.add_cookie(cookie1)
            driver1.refresh()
            time.sleep(3)
        except:
            print(f"--profile {profile} Not add cookie--")
            print("=======================================================================")
            driver1.quit()
            continue
        
        
        #! check like
        try:
            driver1.find_element(by=By.XPATH, value="//i[@id='MBackNavBarLeftArrow']")
        except:
            add_table_profile_ck = [profile ,get_uid ,"" ,"check point"]
            datatable.append(add_table_profile_ck)
            print(f"--profile {profile} check point--")
            print("=======================================================================")
            driver1.quit()
            continue
        time.sleep(random.uniform(0.1, 0.5))
        
        #! count
        num_join = 0
        CP_comment = False
        # print("comment_stop =", comment_stop)
        
        for s in range (0, (len(group_id))):
            
            #! open group
            driver1.get(url+group_id[s])
            time.sleep(random.uniform(3, 4))
            
            #! check like
            try:
                driver1.find_element(by=By.XPATH, value="//i[@id='MBackNavBarLeftArrow']")
            except:
                add_table_profile_ck = [profile ,get_uid ,"" ,"check point"]
                datatable.append(add_table_profile_ck)
                print(f"--profile {profile} check point--")
                print("=======================================================================")
                driver1.quit()
                break
            
            #! find tabcomment and click
            try:
                join_button =  driver1.find_element(by=By.XPATH, value="//button[normalize-space()='Join Group']")
                join_button.click()
                num_join += 1
                join_group_all += 1
                time_sent = (datetime.now().strftime("%H:%M"))
                time_sent = str(time_sent)
                print(f"--profile {profile} join {join_group_all} group / {time_sent} --")
                print("-----------------------------------------------------------------------")
            except:
                continue
            
            time.sleep(random.uniform(10, 35))
            #! screenshot
            try:
                time_af = (datetime.now().strftime("%H:%M"))
                time_af = str(time_af).replace(":", ".")
                driver1.save_screenshot(f"real_use\\joingroup\\img\\profile{profile}_{join_group_all}_{time_af}.png")
            except:
                print("Not screenshot")
        #! add data table
        if CP_comment == False:
            add_table_complete = [profile ,get_uid ,num_join ,"complete"]
            datatable.append(add_table_complete)
        driver1.quit()
    
    #! line notify
    line.sendtext(f"เข้าร่วมกลุ่มสำเร็จ\n-จำนวนกลุ่มที่เข้าร่วม {len(group_id)} กลุ่ม")    
    line.sendsticker(random_complat[0], random_complat[1])
    #! add data table SUM
    add_table_sum = ["SUM" ,num_openprofile ,join_group_all ,"Complete"]
    datatable.append(add_table_sum)
    
    #! show data table
    col_names = ["PROFILE","UID" ,"JOIN_GROUP" , "status"]
    print(tabulate(datatable, headers=col_names, tablefmt="fancy_grid"))

# join_group()