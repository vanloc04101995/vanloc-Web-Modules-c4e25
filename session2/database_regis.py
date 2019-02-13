import mlab
from register import Register

mlab.connect()

# Create
# 1.1. create a food data
r = Register(username = "vanloc04101994", password="Nguyenvanloc1994")
#1.2 save it 
r.save()

# 2 .read
# 2.1. Get cursor
# r_objects = Register.objects() # same as list
# Lazy loading
# 2.2. precess cursor 
# r_first = r_objects[0] # actual data transfering

# print(len(r_objects)) minh dem se lau hon nen ra lenh cho database dem
# database dem
# print(r_objects.count())

#get all data in list
# for r in r_objects:
#     print(r.username)
#     print(r.password)

# r = r_objects[3]
# r.update(set__username = "Banh rat ngon", set__password="Link ngon")
# # neu chua reload thi chi thay doi tren database
# r.reload()
# r.delete()

# delete by Id

# r = r_objects.with_if("5c4d7df944bb8c14dc89fa50")
# if r != None:
#     r.delete()
#     print("OK")
# else: 
#     print("Not found")