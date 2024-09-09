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
from tabulate import tabulate
from selenium.webdriver.chrome.service import Service


def run_login():
    #Get full path program.
    Fullpath = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))


    UnCodeKey = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "@"]


    #input number  profiles // Browser
    Profile_start = int(input("input profiles start : "))
    Profile_end = int(input("input profiles stop : "))
    Browser = (input("1.www || 2.mobile : "))
    print(Browser)
    if Browser == "1":
        Browser = "https://www.facebook.com"
    else:
        Browser = "https://mobile.facebook.com"
    print(Browser)
    
    #! random profile
    sum_ran_p = (Profile_end-Profile_start)+1
    Profile = random.sample(range(Profile_start, (Profile_end+1)), sum_ran_p)
    Profile.sort()
    
    #data table
    datatable =  []

    #1---------------------------------------------------------------
    if 1 in Profile:
        #read chromename or create 
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome1", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome1", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()
        #openbrowser
        opt1 = Options()
        opt1.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt1.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt1.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt1.add_argument(f'--profile-directory={strings}')
        opt1.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt1.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt1.add_argument("--disable-notifications")
        opt1.add_argument("--disable-infobars")
        opt1.add_argument("--window-size=360,720")
        opt1.add_argument("--window-position=3,4")
        driver1 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt1)
        driver1.get(Browser)
        
        # driver1.close()
    #2---------------------------------------------------------------
    if 2 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome2", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome2", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt2 = Options()
        opt2.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt2.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt2.add_argument(f'--profile-directory={strings}')
        opt2.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt2.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt2.add_argument("--disable-notifications")
        opt2.add_argument("--disable-infobars")
        opt2.add_argument("--window-size=360,720")
        opt2.add_argument("--window-position=23,36")
        driver2 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt2)
        driver2.get(Browser)
        
    #3---------------------------------------------------------------
    if 3 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome3", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome3", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt3 = Options()
        opt3.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt3.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt3.add_argument(f'--profile-directory={strings}')
        opt3.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt3.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt3.add_argument("--disable-notifications")
        opt3.add_argument("--disable-infobars")
        opt3.add_argument("--window-size=360,720")
        opt3.add_argument("--window-position=41,67")
        driver3 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt3)
        driver3.get(Browser)
        
    #4---------------------------------------------------------------
    if 4 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome4", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome4", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt4 = Options()
        opt4.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt4.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt4.add_argument(f'--profile-directory={strings}')
        opt4.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt4.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt4.add_argument("--disable-notifications")
        opt4.add_argument("--disable-infobars")
        opt4.add_argument("--window-size=360,720")
        opt4.add_argument("--window-position=64,98")
        driver4 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt4)
        driver4.get(Browser)
        
    #5---------------------------------------------------------------
    if 5 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome5", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome5", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt5 = Options()
        opt5.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt5.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt5.add_argument(f'--profile-directory={strings}')
        opt5.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt5.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt5.add_argument("--disable-notifications")
        opt5.add_argument("--disable-infobars")
        opt5.add_argument("--window-size=360,720")
        opt5.add_argument("--window-position=82,134")
        driver5 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt5)
        driver5.get(Browser)
        
    #6---------------------------------------------------------------
    if 6 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome6", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome6", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt6 = Options()
        opt6.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt6.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt6.add_argument(f'--profile-directory={strings}')
        opt6.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt6.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt6.add_argument("--disable-notifications")
        opt6.add_argument("--disable-infobars")
        opt6.add_argument("--window-size=360,720")
        opt6.add_argument("--window-position=101,165")
        driver6 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt6)
        driver6.get(Browser)
        
    #7---------------------------------------------------------------
    if 7 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome7", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome7", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt7 = Options()
        opt7.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt7.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt7.add_argument(f'--profile-directory={strings}')
        opt7.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt7.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt7.add_argument("--disable-notifications")
        opt7.add_argument("--disable-infobars")
        opt7.add_argument("--window-size=360,720")
        opt7.add_argument("--window-position=121,198")
        driver7 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt7)
        driver7.get(Browser)
        
    #8---------------------------------------------------------------
    if 8 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome8", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome8", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt8 = Options()
        opt8.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt8.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt8.add_argument(f'--profile-directory={strings}')
        opt8.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt8.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt8.add_argument("--disable-notifications")
        opt8.add_argument("--disable-infobars")
        opt8.add_argument("--window-size=360,720")
        opt8.add_argument("--window-position=141,231")
        driver8 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt8)
        driver8.get(Browser)
        
    #9---------------------------------------------------------------
    if 9 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome9", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome9", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt9 = Options()
        opt9.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt9.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt9.add_argument(f'--profile-directory={strings}')
        opt9.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt9.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt9.add_argument("--disable-notifications")
        opt9.add_argument("--disable-infobars")
        opt9.add_argument("--window-size=360,720")
        opt9.add_argument("--window-position=163,264")
        driver9 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt9)
        driver9.get(Browser)
        
    #10---------------------------------------------------------------
    if 10 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome10", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome10", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt10 = Options()
        opt10.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt10.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt10.add_argument(f'--profile-directory={strings}')
        opt10.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt10.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt10.add_argument("--disable-notifications")
        opt10.add_argument("--disable-infobars")
        opt10.add_argument("--window-size=360,720")
        opt10.add_argument("--window-position=183,293")
        driver10 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt10)
        driver10.get(Browser)
        
    #11---------------------------------------------------------------
    if 11 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome11", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome11", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt11 = Options()
        opt11.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt11.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt11.add_argument(f'--profile-directory={strings}')
        opt11.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt11.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt11.add_argument("--disable-notifications")
        opt11.add_argument("--disable-infobars")
        opt11.add_argument("--window-size=360,720")
        opt11.add_argument("--window-position=200,327")
        driver11 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt11)
        driver11.get(Browser)
        
    #12---------------------------------------------------------------
    if 12 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome12", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome12", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt12 = Options()
        opt12.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt12.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt12.add_argument(f'--profile-directory={strings}')
        opt12.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt12.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt12.add_argument("--disable-notifications")
        opt12.add_argument("--disable-infobars")
        opt12.add_argument("--window-size=360,720")
        opt12.add_argument("--window-position=223,356")
        driver12 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt12)
        driver12.get(Browser)
        
    #13---------------------------------------------------------------
    if 13 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome13", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome13", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt13 = Options()
        opt13.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt13.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt13.add_argument(f'--profile-directory={strings}')
        opt13.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt13.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt13.add_argument("--disable-notifications")
        opt13.add_argument("--disable-infobars")
        opt13.add_argument("--window-size=360,720")
        opt13.add_argument("--window-position=607,3")
        driver13 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt13)
        driver13.get(Browser)
        
    #14---------------------------------------------------------------
    if 14 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome14", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome14", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt14 = Options()
        opt14.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt14.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt14.add_argument(f'--profile-directory={strings}')
        opt14.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt14.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt14.add_argument("--disable-notifications")
        opt14.add_argument("--disable-infobars")
        opt14.add_argument("--window-size=360,720")
        opt14.add_argument("--window-position=630,28")
        driver14 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt14)
        driver14.get(Browser)
        
    #15---------------------------------------------------------------
    if 15 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome15", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome15", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt15 = Options()
        opt15.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt15.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt15.add_argument(f'--profile-directory={strings}')
        opt15.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt15.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt15.add_argument("--disable-notifications")
        opt15.add_argument("--disable-infobars")
        opt15.add_argument("--window-size=360,720")
        opt15.add_argument("--window-position=656,55")
        driver15 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt15)
        driver15.get(Browser)
        
    #16---------------------------------------------------------------
    if 16 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome16", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome16", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt16 = Options()
        opt16.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt16.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt16.add_argument(f'--profile-directory={strings}')
        opt16.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt16.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt16.add_argument("--disable-notifications")
        opt16.add_argument("--disable-infobars")
        opt16.add_argument("--window-size=360,720")
        opt16.add_argument("--window-position=681,84")
        driver16 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt16)
        driver16.get(Browser)
        
    #17---------------------------------------------------------------
    if 17 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome17", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome17", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt17 = Options()
        opt17.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt17.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt17.add_argument(f'--profile-directory={strings}')
        opt17.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt17.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt17.add_argument("--disable-notifications")
        opt17.add_argument("--disable-infobars")
        opt17.add_argument("--window-size=360,720")
        opt17.add_argument("--window-position=708,110")
        driver17 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt17)
        driver17.get(Browser)
        
    #18---------------------------------------------------------------
    if 18 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome18", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome18", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt18 = Options()
        opt18.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt18.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt18.add_argument(f'--profile-directory={strings}')
        opt18.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt18.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt18.add_argument("--disable-notifications")
        opt18.add_argument("--disable-infobars")
        opt18.add_argument("--window-size=360,720")
        opt18.add_argument("--window-position=734,136")
        driver18 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt18)
        driver18.get(Browser)
        
    #19---------------------------------------------------------------
    if 19 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome19", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome19", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt19 = Options()
        opt19.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt19.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt19.add_argument(f'--profile-directory={strings}')
        opt19.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt19.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt19.add_argument("--disable-notifications")
        opt19.add_argument("--disable-infobars")
        opt19.add_argument("--window-size=360,720")
        opt19.add_argument("--window-position=759,164")
        driver19 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt19)
        driver19.get(Browser)
        
    #20---------------------------------------------------------------
    if 20 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome20", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome20", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt20 = Options()
        opt20.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt20.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt20.add_argument(f'--profile-directory={strings}')
        opt20.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt20.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt20.add_argument("--disable-notifications")
        opt20.add_argument("--disable-infobars")
        opt20.add_argument("--window-size=360,720")
        opt20.add_argument("--window-position=784,190")
        driver20 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt20)
        driver20.get(Browser)
        
    #21---------------------------------------------------------------
    if 21 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome21", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome21", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt21 = Options()
        opt21.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt21.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt21.add_argument(f'--profile-directory={strings}')
        opt21.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt21.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt21.add_argument("--disable-notifications")
        opt21.add_argument("--disable-infobars")
        opt21.add_argument("--window-size=360,720")
        opt21.add_argument("--window-position=811,215")
        driver21 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt21)
        driver21.get(Browser)
        
    #22---------------------------------------------------------------
    if 22 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome22", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome22", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt22 = Options()
        opt22.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt22.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt22.add_argument(f'--profile-directory={strings}')
        opt22.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt22.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt22.add_argument("--disable-notifications")
        opt22.add_argument("--disable-infobars")
        opt22.add_argument("--window-size=360,720")
        opt22.add_argument("--window-position=835,245")
        driver22 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt22)
        driver22.get(Browser)
        
    #23---------------------------------------------------------------
    if 23 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome23", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome23", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt23 = Options()
        opt23.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt23.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt23.add_argument(f'--profile-directory={strings}')
        opt23.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt23.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt23.add_argument("--disable-notifications")
        opt23.add_argument("--disable-infobars")
        opt23.add_argument("--window-size=360,720")
        opt23.add_argument("--window-position=860,270")
        driver23 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt23)
        driver23.get(Browser)
        
    #24---------------------------------------------------------------
    if 24 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome24", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome24", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt24 = Options()
        opt24.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt24.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt24.add_argument(f'--profile-directory={strings}')
        opt24.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt24.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt24.add_argument("--disable-notifications")
        opt24.add_argument("--disable-infobars")
        opt24.add_argument("--window-size=360,720")
        opt24.add_argument("--window-position=886,296")
        driver24 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt24)
        driver24.get(Browser)
        
    #25---------------------------------------------------------------
    if 25 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome25", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome25", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt25 = Options()
        opt25.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt25.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt25.add_argument(f'--profile-directory={strings}')
        opt25.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt25.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt25.add_argument("--disable-notifications")
        opt25.add_argument("--disable-infobars")
        opt25.add_argument("--window-size=360,720")
        opt25.add_argument("--window-position=911,324")
        driver25 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt25)
        driver25.get(Browser)
        
    #26---------------------------------------------------------------
    if 26 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome26", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome26", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt26 = Options()
        opt26.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt26.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt26.add_argument(f'--profile-directory={strings}')
        opt26.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt26.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt26.add_argument("--disable-notifications")
        opt26.add_argument("--disable-infobars")
        opt26.add_argument("--window-size=360,720")
        opt26.add_argument("--window-position=940,349")
        driver26 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt26)
        driver26.get(Browser)
        
    #27---------------------------------------------------------------
    if 27 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome27", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome27", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt27 = Options()
        opt27.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt27.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt27.add_argument(f'--profile-directory={strings}')
        opt27.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt27.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt27.add_argument("--disable-notifications")
        opt27.add_argument("--disable-infobars")
        opt27.add_argument("--window-size=360,720")
        opt27.add_argument("--window-position=1234,7")
        driver27 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt27)
        driver27.get(Browser)
        
    #28---------------------------------------------------------------
    if 28 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome28", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome28", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt28 = Options()
        opt28.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt28.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt28.add_argument(f'--profile-directory={strings}')
        opt28.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt28.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt28.add_argument("--disable-notifications")
        opt28.add_argument("--disable-infobars")
        opt28.add_argument("--window-size=360,720")
        opt28.add_argument("--window-position=1258,34")
        driver28 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt28)
        driver28.get(Browser)
        
    #29---------------------------------------------------------------
    if 29 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome29", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome29", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt29 = Options()
        opt29.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt29.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt29.add_argument(f'--profile-directory={strings}')
        opt29.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt29.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt29.add_argument("--disable-notifications")
        opt29.add_argument("--disable-infobars")
        opt29.add_argument("--window-size=360,720")
        opt29.add_argument("--window-position=1286,59")
        driver29 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt29)
        driver29.get(Browser)
        
    #30---------------------------------------------------------------
    if 30 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome30", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome30", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt30 = Options()
        opt30.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt30.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt30.add_argument(f'--profile-directory={strings}')
        opt30.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt30.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt30.add_argument("--disable-notifications")
        opt30.add_argument("--disable-infobars")
        opt30.add_argument("--window-size=360,720")
        opt30.add_argument("--window-position=1308,83")
        driver30 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt30)
        driver30.get(Browser)
        
    #31---------------------------------------------------------------
    if 31 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome31", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome31", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt31 = Options()
        opt31.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt31.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt31.add_argument(f'--profile-directory={strings}')
        opt31.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt31.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt31.add_argument("--disable-notifications")
        opt31.add_argument("--disable-infobars")
        opt31.add_argument("--window-size=360,720")
        opt31.add_argument("--window-position=1332,112")
        driver31 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt31)
        driver31.get(Browser)
        
    #32---------------------------------------------------------------
    if 32 in Profile:
        try:
            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome32", "r")
            strings = filetxt.read()
            filetxt.close()
        except:
            strings = ''
            for m in range(10):
                strings += f"{random.choice(UnCodeKey)}"

            filetxt = open(f"{Fullpath}\\chrome_name\\use_profile_namechrome32", "w+")
            filetxt.write(f"{strings}")
            filetxt.close()

        opt32 = Options()
        opt32.add_argument(r"--user-data-dir={}\\chrome\\{}".format(Fullpath, strings))
        opt32.add_argument(f"--load-extension={Fullpath}\\assets\\getcookie")
        opt32.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt32.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt32.add_argument("--disable-notifications")
        opt32.add_argument("--disable-infobars")
        opt32.add_argument("--window-size=360,720")
        opt32.add_argument("--window-position=1356,135")
        driver32 = webdriver.Chrome(service=Service(executable_path="./assets/chromedriver.exe"), options=opt32)
        driver32.get(Browser)
        

    # get cookie
    get_ck = input(" get cookies press *1* : ")
    if get_ck == "1":
        if 1 in Profile:
            # get cookie
            pickle.dump( driver1.get_cookies() , open(f"{Fullpath}\\cookie\\cookies1.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies1.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver1.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([1, uid, "live"])
            except:
                datatable.append([1, uid, "checkpoint"])
            

            
        if 2 in Profile:  
            # get cookie
            pickle.dump( driver2.get_cookies() , open(f"{Fullpath}\\cookie\\cookies2.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies2.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver2.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([2, uid, "live"])
            except:
                datatable.append([2, uid, "checkpoint"])
            
        if 3 in Profile:
            # get cookie
            pickle.dump( driver3.get_cookies() , open(f"{Fullpath}\\cookie\\cookies3.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies3.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver3.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([3, uid, "live"])
            except:
                datatable.append([3, uid, "checkpoint"])
            
        if 4 in Profile:
            # get cookie
            pickle.dump( driver4.get_cookies() , open(f"{Fullpath}\\cookie\\cookies4.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies4.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver4.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([4, uid, "live"])
            except:
                datatable.append([4, uid, "checkpoint"])     
            
        if 5 in Profile:
            # get cookie
            pickle.dump( driver5.get_cookies() , open(f"{Fullpath}\\cookie\\cookies5.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies5.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver5.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([5, uid, "live"])
            except:
                datatable.append([5, uid, "checkpoint"])     
            
        if 6 in Profile:
            # get cookie
            pickle.dump( driver6.get_cookies() , open(f"{Fullpath}\\cookie\\cookies6.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies6.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver6.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([6, uid, "live"])
            except:
                datatable.append([6, uid, "checkpoint"])  
            
        if 7 in Profile:
            # get cookie
            pickle.dump( driver7.get_cookies() , open(f"{Fullpath}\\cookie\\cookies7.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies7.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver7.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([7, uid, "live"])
            except:
                datatable.append([7, uid, "checkpoint"])

        if 8 in Profile:
            # get cookie
            pickle.dump( driver8.get_cookies() , open(f"{Fullpath}\\cookie\\cookies8.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies8.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver8.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([8, uid, "live"])
            except:
                datatable.append([8, uid, "checkpoint"])   

        if 9 in Profile:
            # get cookie
            pickle.dump( driver9.get_cookies() , open(f"{Fullpath}\\cookie\\cookies9.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies9.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver9.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([9, uid, "live"])
            except:
                datatable.append([9, uid, "checkpoint"])   

        if 10 in Profile:
            # get cookie
            pickle.dump( driver10.get_cookies() , open(f"{Fullpath}\\cookie\\cookies10.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies10.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver10.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([10, uid, "live"])
            except:
                datatable.append([10, uid, "checkpoint"])

        if 11 in Profile:
            # get cookie
            pickle.dump( driver11.get_cookies() , open(f"{Fullpath}\\cookie\\cookies11.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies11.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver11.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([11, uid, "live"])
            except:
                datatable.append([11, uid, "checkpoint"])

        if 12 in Profile:
            # get cookie
            pickle.dump( driver12.get_cookies() , open(f"{Fullpath}\\cookie\\cookies12.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies12.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver12.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([12, uid, "live"])
            except:
                datatable.append([12, uid, "checkpoint"])

        if 13 in Profile:
            # get cookie
            pickle.dump( driver13.get_cookies() , open(f"{Fullpath}\\cookie\\cookies13.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies13.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver13.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([13, uid, "live"])
            except:
                datatable.append([13, uid, "checkpoint"])

        if 14 in Profile:
            # get cookie
            pickle.dump( driver14.get_cookies() , open(f"{Fullpath}\\cookie\\cookies14.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies14.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver14.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([14, uid, "live"])
            except:
                datatable.append([14, uid, "checkpoint"])

        if 15 in Profile:
            # get cookie
            pickle.dump( driver15.get_cookies() , open(f"{Fullpath}\\cookie\\cookies15.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies15.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver15.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([15, uid, "live"])
            except:
                datatable.append([15, uid, "checkpoint"])

        if 16 in Profile:
            # get cookie
            pickle.dump( driver16.get_cookies() , open(f"{Fullpath}\\cookie\\cookies16.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies16.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver16.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([16, uid, "live"])
            except:
                datatable.append([16, uid, "checkpoint"])

        if 17 in Profile:
            # get cookie
            pickle.dump( driver17.get_cookies() , open(f"{Fullpath}\\cookie\\cookies17.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies17.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver17.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([17, uid, "live"])
            except:
                datatable.append([17, uid, "checkpoint"])

        if 18 in Profile:
            # get cookie
            pickle.dump( driver18.get_cookies() , open(f"{Fullpath}\\cookie\\cookies18.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies18.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver18.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([18, uid, "live"])
            except:
                datatable.append([18, uid, "checkpoint"])

        if 19 in Profile:
            # get cookie
            pickle.dump( driver19.get_cookies() , open(f"{Fullpath}\\cookie\\cookies19.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies19.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver19.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([19, uid, "live"])
            except:
                datatable.append([19, uid, "checkpoint"])

        if 20 in Profile:
            # get cookie
            pickle.dump( driver20.get_cookies() , open(f"{Fullpath}\\cookie\\cookies20.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies20.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver20.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([20, uid, "live"])
            except:
                datatable.append([20, uid, "checkpoint"])
            
        if 21 in Profile:
            # get cookie
            pickle.dump( driver21.get_cookies() , open(f"{Fullpath}\\cookie\\cookies21.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies21.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver21.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([21, uid, "live"])
            except:
                datatable.append([21, uid, "checkpoint"])

        if 22 in Profile:
            # get cookie
            pickle.dump( driver22.get_cookies() , open(f"{Fullpath}\\cookie\\cookies22.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies22.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver22.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([22, uid, "live"])
            except:
                datatable.append([22, uid, "checkpoint"])
            
        if 23 in Profile:
            # get cookie
            pickle.dump( driver23.get_cookies() , open(f"{Fullpath}\\cookie\\cookies23.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies23.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver23.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([23, uid, "live"])
            except:
                datatable.append([23, uid, "checkpoint"])

        if 24 in Profile:
            # get cookie
            pickle.dump( driver24.get_cookies() , open(f"{Fullpath}\\cookie\\cookies24.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies24.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver24.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([24, uid, "live"])
            except:
                datatable.append([24, uid, "checkpoint"])

        if 25 in Profile:
            # get cookie
            pickle.dump( driver25.get_cookies() , open(f"{Fullpath}\\cookie\\cookies25.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies25.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver25.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([25, uid, "live"])
            except:
                datatable.append([25, uid, "checkpoint"])
            
        if 26 in Profile:
            # get cookie
            pickle.dump( driver26.get_cookies() , open(f"{Fullpath}\\cookie\\cookies26.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies26.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver26.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([26, uid, "live"])
            except:
                datatable.append([26, uid, "checkpoint"])

        if 27 in Profile:
            # get cookie
            pickle.dump( driver27.get_cookies() , open(f"{Fullpath}\\cookie\\cookies27.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies27.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver27.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([27, uid, "live"])
            except:
                datatable.append([27, uid, "checkpoint"])

        if 28 in Profile:
            # get cookie
            pickle.dump( driver28.get_cookies() , open(f"{Fullpath}\\cookie\\cookies28.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies28.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver28.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([28, uid, "live"])
            except:
                datatable.append([28, uid, "checkpoint"])

        if 29 in Profile:
            # get cookie
            pickle.dump( driver29.get_cookies() , open(f"{Fullpath}\\cookie\\cookies29.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies29.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver29.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([29, uid, "live"])
            except:
                datatable.append([29, uid, "checkpoint"])

        if 30 in Profile:
            # get cookie
            pickle.dump( driver30.get_cookies() , open(f"{Fullpath}\\cookie\\cookies30.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies30.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver30.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([30, uid, "live"])
            except:
                datatable.append([30, uid, "checkpoint"])

        if 31 in Profile:
            # get cookie
            pickle.dump( driver31.get_cookies() , open(f"{Fullpath}\\cookie\\cookies31.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies31.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver31.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([31, uid, "live"])
            except:
                datatable.append([31, uid, "checkpoint"])

        if 32 in Profile:
            # get cookie
            pickle.dump( driver32.get_cookies() , open(f"{Fullpath}\\cookie\\cookies32.pkl","wb"))
            #get uid
            cookies = pickle.load(open(f"{Fullpath}\\cookie\\cookies32.pkl", "rb"))
            cookie_str = (str(cookies))
            cookie_split = cookie_str.split(',')
            for i in cookie_split:
                if "1000" in i:
                    cookie_str = str(i)
                    uid = (cookie_str.replace("'", "").replace(":", "").replace("}", "").replace("value", "").replace("]", ""))
                    break
            # check live
            try:
                driver32.find_element(by=By.XPATH, value="//span[normalize-space()='News Feed']/following-sibling::div")
                datatable.append([32, uid, "live"])
            except:
                datatable.append([32, uid, "checkpoint"])

        #show table
        col_names = ["profile", "uid", "status"]
        print(tabulate(datatable, headers=col_names, tablefmt="fancy_grid"))
        
        
run_login()