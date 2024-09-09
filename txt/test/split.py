spi = ['บอ.บู๋ พบประชาชน\nSports ', ' 5 out of 5 ', ' 94K followers ', ' 10+ posts in the last 2 weeks\nเกิดมาไม่เคยรักใครเท่านี้เลย แต่เธ\nFollow']

# for sp in spi:
#     if ("followers" in sp and "M" in sp)  or ("followers" in sp and "K" in sp) or ("likes" in sp and "K" in sp) or ("likes" in sp and "M" in sp):
#         data_str = str(sp)
#         page_follower = data_str.replace("likes", "").replace("followers", "").replace(" ", "")
#         if "K" in page_follower:
#             number = 1000
#         elif "M" in page_follower:
#             number = 1000000
#         else:
#             pass
#         page_follower = data_str.replace("M", "").replace("K", "").replace("likes", "").replace("followers", " ").replace(" ", "")
#         page_follower = (float(page_follower)*number)
# print(page_follower)


for sp in spi:
    if ("followers" in sp and "M" in sp)  or ("followers" in sp and "K" in sp) or ("likes" in sp and "K" in sp) or ("likes" in sp and "M" in sp):
        data_str = str(sp)
        if "\n" in data_str:
            data_str = data_str.split('\n')
            del data_str[1:]
            data_str = str(data_str).replace("['", "").replace("']", "").replace(" ", "")
        else:
            pass
        page_follower = data_str.replace("likes", "").replace("followers", "").replace(" ", "")
        if "K" in page_follower:
            number = 1000
        elif "M" in page_follower:
            number = 1000000
        else:
            number = 1
        page_follower = data_str.replace("M", "").replace("K", "").replace("likes", "").replace("followers", " ").replace(" ", "")
        page_follower = (float(page_follower)*number)
    elif "followers" in sp or "likes" in sp:
        data_str = str(sp)
        if "\n" in data_str:
            data_str = data_str.split('\n')
            del data_str[1:]
            data_str = str(data_str).replace("['", "").replace("']", "").replace(" ", "")
        else:
            pass
        page_follower = data_str.replace("likes", "").replace("followers", "").replace(" ", "")
        if "K" in page_follower:
            number = 1000
        elif "M" in page_follower:
            number = 1000000
        else:
            number = 1
        page_follower = data_str.replace("M", "").replace("K", "").replace("likes", "").replace("followers", " ").replace(" ", "")
        page_follower = (float(page_follower)*number)
        
# print(data_str)
# print(type(data_str))
print(page_follower)
# print(type(page_follower))

# print(number)
