import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from urllib.request import urlopen
import os
import sys
from os import path
import random
import pickle
from selenium.webdriver.chrome.service import Service
#! from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm
from time import sleep
import threading
import xlsxwriter
from parinya import LINE

def scrping_groupid():

    #!Get full path program.
    Fullpath = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))
    #!print(Fullpath)

    UnCodeKey = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "@"]

    #!input Profile  and uid
    input_Profile = str(input("profile to use : "))
    key_word = str(input("key word : "))
    url = (f"https://www.facebook.com/search/groups?q={key_word}")
    Minimum_followers = int(input("Minimum_followers : "))
    
    #! read line key
    filetxt_line_key = open("line_key.txt", "r",encoding='utf-8')
    line_key = ""
    line_key = filetxt_line_key.read()
    filetxt_line_key.close()
    #! select stiker
    list_await = [[1, 103], [1, 1], [1, 402], [1, 404], [1, 404], [1, 424], [1, 430], [2, 140], [2, 155], [2, 502], [2, 503], [2, 513], [2, 512], [2, 524]]
    list_complat = [[1, 106], [1, 116], [1, 41], [1, 413], [2, 28], [2, 40], [2, 41], [2, 45], [2, 147], [2, 527]]
    random_await = (random.choice(list_await))
    random_complat = (random.choice(list_complat))

    #!read file chrome
    try:
        filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome{input_Profile}", "r")
        strings = filetxt.read()
        filetxt.close()
    except:
        strings = ''
        for m in range(10):
            strings += f"{random.choice(UnCodeKey)}"

        filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome{input_Profile}", "w+")
        filetxt.write(f"{strings}")
        filetxt.close()

    #!open chrome
    opt1 = Options()
    opt1.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
    opt1.add_argument(f'--profile-directory={strings}')
    #! opt1.add_argument("--start-maximized")
    opt1.add_experimental_option("excludeSwitches", ['enable-automation'])
    opt1.add_argument("--disable-notifications")
    opt1.add_argument("--disable-infobars")
    opt1.add_argument("--window-size=360,640")
    opt1.add_experimental_option('excludeSwitches', ['enable-logging'])
    opt1.add_argument('--headless')
    #! driver1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt1)
    driver1 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt1)
    

    driver1.get(url)
    #! driver1.maximize_window()
    time.sleep(1)

    #!add cookie
    try:
        cookies1 = pickle.load(open(f"{Fullpath}\\cookie\\cookies{input_Profile}.pkl", "rb"))
        for cookie1 in cookies1:
            driver1.add_cookie(cookie1)
        driver1.refresh()
    except:
        print("Not add cookie")
        print("------------------------------------------------------------------------")

    #! line notify
    input_line_key = line_key
    line = LINE(input_line_key)

    #!select Public Groups
    try:
        Public_Groups = driver1.find_element(by=By.XPATH, value="//div//input[@aria-label='Public Groups']")
        driver1.execute_script("arguments[0].scrollIntoView(true);", Public_Groups)
        time.sleep(0.50)
        Public_Groups.click()
        time.sleep(2.50)
        driver1.refresh()
        time.sleep(2.50)
    except:
        print("Not select Public Groups")
        print("------------------------------------------------------------------------")
        driver1.quit()

    #! count
    data_exc = []
    num_getuid = 0
    start = 0
    num_getuid_r = 0

    print("------------------------------------------------------------------------")
    print("<<--await-->>")
    line.sendtext(f"กำลังดำเนินการเก็บข้อมูลเพจ {key_word} ที่มียอดfollower {Minimum_followers} ขึ้นไป กรุณารอสักครู่")
    line.sendsticker(random_await[0], random_await[1])
    print("------------------------------------------------------------------------")

    while True:
        #!get uid
        try:
            url_page = driver1.find_elements(by=By.XPATH, value="//div[@role='article']//a[@aria-hidden='true']")
            name_page = driver1.find_elements(by=By.XPATH, value="//div[@role='article']//a[@aria-hidden='true']")
            des_page = driver1.find_elements(by=By.XPATH, value="//div[@role='article']")
            # print("name_page = ", len(name_page))
            # print("---------------------------------------------")
        except:
            print(f"Error find xpath")
        for i in range(start , len(name_page)):
            #!scroll
            driver1.execute_script("arguments[0].scrollIntoView(true);", name_page[i])
            # print("i", i)
            try:
                #!record uid
                # print("num_getuid = ", num_getuid)
                num_getuid += 1
                get_urlpage = url_page[i].get_attribute('href').replace("https://www.facebook.com/groups", "").replace("/", "")
                get_namegroup = name_page[i].text
                #!despage split
                get_despage = des_page[i].text.split("·")
                get_despage2 = des_page[i].text.split("·")
                page_fol = 0
                number = 1
            except:
                print("Error get data")
                print("------------------------------------------------------------------------")
            #!split number follower
            try:
                for sp in get_despage:
                    if ("members" in sp and "M" in sp)  or ("members" in sp and "K" in sp):
                        data_str = str(sp)
                        if "\n" in data_str:
                            data_str = data_str.split('\n')
                            del data_str[1:]
                            data_str = str(data_str).replace("['", "").replace("']", "").replace(" ", "")
                        else:
                            pass
                        page_follower = data_str.replace("members", "").replace(" ", "")
                        if "K" in page_follower:
                            number = 1000
                        elif "M" in page_follower:
                            number = 1000000
                        else:
                            number = 1
                        page_follower = data_str.replace("M", "").replace("K", "").replace("members", " ").replace(" ", "")
                        page_fol = (float(page_follower)*number)
                    elif "members" in sp:
                        data_str = str(sp)
                        if "\n" in data_str:
                            data_str = data_str.split('\n')
                            del data_str[1:]
                            data_str = str(data_str).replace("['", "").replace("']", "").replace(" ", "")
                        else:
                            pass
                        page_follower = data_str.replace("members", "").replace(" ", "")
                        if "K" in page_follower:
                            number = 1000
                        elif "M" in page_follower:
                            number = 1000000
                        else:
                            number = 1
                        page_follower = data_str.replace("M", "").replace("K", "").replace("likes", "").replace("members", " ").replace(" ", "")
                        page_fol = (float(page_follower)*number)
            except:
                try:
                    del get_despage2[-1]
                    for sp in get_despage2:
                        if ("members" in sp):
                            data_str = str(sp)
                            page_follower = data_str.replace("members", "").replace(" ", "")
                            if "K" in page_follower:
                                number = 1000
                            elif "M" in page_follower:
                                number = 1000000
                            else:
                                pass
                            page_follower = data_str.replace("M", "").replace("K", "").replace("members", "").replace(" ", "")
                            page_fol = (float(page_follower)*number)
                except:
                    print("Err split")
            try:
                if page_fol > Minimum_followers:
                    add_data = [get_urlpage, get_namegroup, page_fol]
                    data_exc.append(add_data)
                    #! Create a workbook and add a worksheet.
                    workbook = xlsxwriter.Workbook(f'{Fullpath}\\real_use\\page_group_id\\Group_id_{key_word}.xlsx')
                    worksheet = workbook.add_worksheet()
                    #! Add a bold format to use to highlight cells.
                    bold = workbook.add_format({'bold': 1})
                    #! Write some data headers.
                    worksheet.write('A1', 'GROUP_ID', bold)
                    worksheet.write('B1', 'GROUP_NAME', bold)
                    worksheet.write('C1', 'FOLLOWER', bold)
                    #! Iterate over the data and write it out row by row.
                    #! Start from the first cell. Rows and columns are zero indexed.
                    row = 1
                    col = 0
                    for url, name, number in (data_exc):
                        worksheet.write(row, col,     url)
                        worksheet.write(row, col + 1, name)
                        worksheet.write(row, col + 2, number)
                        row += 1
                    workbook.close()
                    num_getuid_r += 1
            except:
                print("Error save data to exc")
            # time.sleep(0.50)
            start += 1
            if start == 300:
                print(f"complete Get data all = {num_getuid_r}")
                print("========================================================================")
                line.sendtext(f"ดึงกลุ่ม {key_word} ที่มียอดfollower {Minimum_followers} ขึ้นไป มาได้ทั้งหมด {num_getuid_r} กลุ่ม")
                line.sendsticker(random_complat[0], random_complat[1])
                driver1.quit()
                break
        time.sleep(1)
        if start == 300:
            break
        
# scrping_groupid()

