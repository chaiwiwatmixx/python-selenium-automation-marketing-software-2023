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
# from webdriver_manager.chrome import ChromeDriverManager
from tabulate import tabulate
from tqdm import tqdm
from time import sleep
import threading
from scrping_pageid_addexc import scrping_pageid
from scrping_groupid_addexc import scrping_groupid
from comment_page_new_mul import comment_page
from comment_group_new_mul import comment_group
from post_group import post_group
from join_group import join_group
from Opencookie import run_opencookies
from Opencookie_login import run_login
from check_group2 import check_group
from firebase_admin import credentials, initialize_app, db
import socket


#! get ip
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)


Auth = False

while (True):
    #! login
    username_u = input("user : ")
    input_line_key = str(input("line key notify : "))
    filetxt = open("line_key.txt", "w+")
    filetxt.write(f"{input_line_key}")
    filetxt.close()
    print("-----------------------------------------------------------------------")
    #! check ip
    try:
        if username_u == "kubot1":
            IP_1 = db.reference("kubot1")
            if IPAddr == IP_1.get():
                Auth = True
            else: 
                Auth = True
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot2":
            IP_2 = db.reference("kubot2")
            if IPAddr == IP_2.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot3":
            IP_3 = db.reference("kubot3")
            if IPAddr == IP_3.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot4":
            IP_4 = db.reference("kubot4")
            if IPAddr == IP_4.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot5":
            IP_5 = db.reference("kubot5")
            if IPAddr == IP_5.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot6":
            IP_6 = db.reference("kubot6")
            if IPAddr == IP_6.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot7":
            IP_7 = db.reference("kubot7")
            if IPAddr == IP_7.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot8":
            IP_8 = db.reference("kubot8")
            if IPAddr == IP_8.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot9":
            IP_9 = db.reference("kubot9")
            if IPAddr == IP_9.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot10":
            IP_10 = db.reference("kubot10")
            if IPAddr == IP_10.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot11":
            IP_11 = db.reference("kubot11")
            if IPAddr == IP_11.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot12":
            IP_12 = db.reference("kubot12")
            if IPAddr == IP_12.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot13":
            IP_13 = db.reference("kubot13")
            if IPAddr == IP_13.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot14":
            IP_14 = db.reference("kubot14")
            if IPAddr == IP_14.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot15":
            IP_15 = db.reference("kubot15")
            if IPAddr == IP_15.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot16":
            IP_16 = db.reference("kubot16")
            if IPAddr == IP_16.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot17":
            IP_17 = db.reference("kubot17")
            if IPAddr == IP_17.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot18":
            IP_18 = db.reference("kubot18")
            if IPAddr == IP_18.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot19":
            IP_19 = db.reference("kubot19")
            if IPAddr == IP_19.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot20":
            IP_20 = db.reference("kubot20")
            if IPAddr == IP_20.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot21":
            IP_21 = db.reference("kubot21")
            if IPAddr == IP_21.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot22":
            IP_22 = db.reference("kubot22")
            if IPAddr == IP_22.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot23":
            IP_23 = db.reference("kubot23")
            if IPAddr == IP_23.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot24":
            IP_24 = db.reference("kubot24")
            if IPAddr == IP_24.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot25":
            IP_25 = db.reference("kubot25")
            if IPAddr == IP_25.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot26":
            IP_26 = db.reference("kubot26")
            if IPAddr == IP_26.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot27":
            IP_27 = db.reference("kubot27")
            if IPAddr == IP_27.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot28":
            IP_28 = db.reference("kubot28")
            if IPAddr == IP_28.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot29":
            IP_29 = db.reference("kubot29")
            if IPAddr == IP_29.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot30":
            IP_30 = db.reference("kubot30")
            if IPAddr == IP_30.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot31":
            IP_31 = db.reference("kubot31")
            if IPAddr == IP_31.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot32":
            IP_32 = db.reference("kubot32")
            if IPAddr == IP_32.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot33":
            IP_33 = db.reference("kubot33")
            if IPAddr == IP_33.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot34":
            IP_34 = db.reference("kubot34")
            if IPAddr == IP_34.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot35":
            IP_35 = db.reference("kubot35")
            if IPAddr == IP_35.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot36":
            IP_36 = db.reference("kubot36")
            if IPAddr == IP_36.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot37":
            IP_37 = db.reference("kubot37")
            if IPAddr == IP_37.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot38":
            IP_38 = db.reference("kubot38")
            if IPAddr == IP_38.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot39":
            IP_39 = db.reference("kubot39")
            if IPAddr == IP_39.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot40":
            IP_40 = db.reference("kubot40")
            if IPAddr == IP_40.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot41":
            IP_41 = db.reference("kubot41")
            if IPAddr == IP_41.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot42":
            IP_42 = db.reference("kubot42")
            if IPAddr == IP_42.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot43":
            IP_43 = db.reference("kubot43")
            if IPAddr == IP_43.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot44":
            IP_44 = db.reference("kubot44")
            if IPAddr == IP_44.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot45":
            IP_45 = db.reference("kubot45")
            if IPAddr == IP_45.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot46":
            IP_46 = db.reference("kubot46")
            if IPAddr == IP_46.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot47":
            IP_47 = db.reference("kubot47")
            if IPAddr == IP_47.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot48":
            IP_48 = db.reference("kubot48")
            if IPAddr == IP_48.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot49":
            IP_49 = db.reference("kubot49")
            if IPAddr == IP_49.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        # ----------------------------------------------
        elif username_u == "kubot50":
            IP_50 = db.reference("kubot50")
            if IPAddr == IP_50.get():
                Auth = True
            else: 
                print("ip computer not matching")
                pass
        else:
            print("no user in the system")
            print("-----------------------------------------------------------------------")
    except:
        print("check ip Error")
    # ----------------------------------------------
    if Auth == True:
        while (True):
            #select function
            col_names = ["choice", "function"]
            datatable = [["1", "login"],
                        ["2", "open profile"],
                        ["3", "get pageid"],
                        ["4", "get groupid"],
                        ["5", "spam comment page"],
                        ["6", "spam comment group"],
                        ["7", "check group"],
                        ["8", "spam post group"],
                        ["9", "join group"]]
            print(tabulate(datatable, headers=col_names, tablefmt="fancy_grid"))
            Do_what = input("select number : ")
            print("-------------------------------------------------------------------------------")
            if Do_what == "1":
                print("<<-- Login -->>")
                run_login()
                print("<< Login complete >>")
                print("-------------------------------------------------------------------------------")
            elif Do_what == "2":
                print("<<-- open browser -->>")
                run_opencookies()
                print("<< open profile complete >>")
                print("-------------------------------------------------------------------------------")
            elif Do_what == "3":
                print("<<-- get pageid -->>")
                scrping_pageid()
                print("<< get pageid complete >>")
                print("-------------------------------------------------------------------------------")
            elif Do_what == "4":
                print("<<-- get groupid -->>")
                scrping_groupid()
                print("<< get groupid complete >>")
                print("-------------------------------------------------------------------------------")
            elif Do_what == "5":
                print("<<-- spam comment page -->>")
                comment_page()
                print("<< spam comment page complete >>")
                print("-------------------------------------------------------------------------------")
            elif Do_what == "6":
                print("<<-- spam comment group -->>")
                comment_group()
                print("<< spam comment group complete >>")
                print("-------------------------------------------------------------------------------")
            elif Do_what == "7":
                print("<<-- check group -->>")
                check_group()
                print("<< check group complete >>")
                print("-------------------------------------------------------------------------------")
            elif Do_what == "8":
                print("<<-- spam post group -->>")
                post_group()
                print("<< spam post group complete >>")
                print("-------------------------------------------------------------------------------")
            elif Do_what == "9":
                print("<<-- join group -->>")
                join_group()
                print("<< join group complete >>")
                print("-------------------------------------------------------------------------------")
            else:
                print("<<-- funtion not found -->>")
                print("-------------------------------------------------------------------------------")
    else:
        pass




