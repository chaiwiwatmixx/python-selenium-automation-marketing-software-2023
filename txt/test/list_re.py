import os
import sys
from os import path

#! Get full path program.
Fullpath = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))

remove_groupid = ["1003273896776711", "368796298333625", "447942946738256", "2612909755520707tv"]

group_id_txt = open(f"{Fullpath}\\group_id.txt", "r" ,encoding='utf-8')
group_id = ""
group_id = group_id_txt.read().split("\n")
group_id_txt.close()


for re in range(0, len(remove_groupid)):
    group_id.remove(remove_groupid[re])
    with open(f"{Fullpath}\\group_id.txt","w") as tfile:
        tfile.write('\n'.join(group_id))