comment_txt = open("txt\\comment.txt", "r" ,encoding='utf-8')
comment = ""
comment = comment_txt.read().split("|")
comment_txt.close()

print(comment)