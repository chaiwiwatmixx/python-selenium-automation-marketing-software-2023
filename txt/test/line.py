from parinya import LINE
# import random
import random
  
# select stiker
list1 = [[1, 103], [1, 1], [1, 402], [1, 404], [1, 404], [1, 424], [1, 430], [2, 140], [2, 155], [2, 502], [2, 503], [2, 513], [2, 512], [2, 524]]
random = (random.choice(list1))

line = LINE("bu3myohj4UKV4qbfnp8Pjf4hIf96HBlhd0coGanhogF")
# line.sendtext("สวัสดิดีครับ")
# image = unnamed.png
# line.sendimage("unnamed.png")
line.sendsticker(random[0], random[1])



# bu3myohj4UKV4qbfnp8Pjf4hIf96HBlhd0coGanhogF