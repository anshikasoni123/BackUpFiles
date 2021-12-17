import os
import shutil
import time

days = time.time()
print(days)

path = input("Enter your source folder here :- ")
isExist = os.path.exists(path)
print(isExist)
list = os.listdir(path)
print(list)
join = os.path.join(path)
print(path)
ctime = os.stat(path).st_ctime
print(ctime)

while path == '':
    print("Not Found")