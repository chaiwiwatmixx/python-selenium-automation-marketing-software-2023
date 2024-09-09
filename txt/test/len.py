import random

page_id_txt = open("txt\\page_id.txt", "r")
page_id = ""
page_id = page_id_txt.read().split("\n")
page_id_txt.close()

print(random.randint(0, len(page_id)-1))