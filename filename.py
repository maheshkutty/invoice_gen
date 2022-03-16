import os
import datetime
import time
d = 'Mahesh Kutty'
dateObjFolder = str(datetime.date.today())
parent_directory  = 'D:\Workspace\SPIT\SEM 2\Process automation\Project\client_invoice'
d = d.replace(" ", "_") + "_" + str(int(time.time()))
print(d)
print(int(time.time()))
if os.path.isdir(os.path.join(parent_directory, dateObjFolder)) == False:
    os.makedirs(os.path.join(parent_directory, dateObjFolder))
    print(os.path.join(parent_directory, dateObjFolder))
print(os.path.join(parent_directory, dateObjFolder))