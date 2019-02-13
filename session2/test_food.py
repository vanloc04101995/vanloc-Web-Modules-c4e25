import mlab
from food import Food

mlab.connect()

# Create
# 1.1. create a food data
# f = Food(title = "Banh sai", link="<<Link here>>")
# #1.2 save it 
# f.save()

# 2 .read
# 2.1. Get cursor
f_objects = Food.objects() # same as list
# Lazy loading
# 2.2. precess cursor 
# f_first = f_objects[0] # actual data transfering

# print(len(f_objects)) minh dem se lau hon nen ra lenh cho database dem
# database dem
# print(f_objects.count())

#get all data in list
# for f in f_objects:
#     print(f.title)
#     print(f.link)

# f = f_objects[3]
# f.update(set__title = "Banh rat ngon", set__link="Link ngon")
# # neu chua reload thi chi thay doi tren database
# f.reload()
# f.delete()

# delete by Id

f = f_objects.with_if("5c4d7df944bb8c14dc89fa50")
if f != None:
    f.delete()
    print("OK")
else: 
    print("Not found")