import os, shutil
import datetime as dt

oldest_access_time = dt.date.today()
youngest_access_time = dt.date(2,2,2)
expiration = 30 # 30 days
file_list = []
downloads = "F:\\Downloads\\"
os.chdir(downloads)

# checks if a directory exist, and if it doesn't, it makes it
def cmake_dir(dir):
    if not os.path.isdir(dir):
        try:
            os.mkdir(dir)
        except OSError:
            print ("Creation of the directory %s failed" % dir)
        else:
            print ("Successfully created the directory %s " % dir)
def setYoungestATime(date):
    global youngest_access_time
    if date > youngest_access_time:
        youngest_access_time = date
def getYoungestATime():
    global youngest_access_time
    return youngest_access_time
def setOldestATime(date):
    global oldest_access_time
    if date < getOldestATime():
        oldest_access_time = date
def getOldestATime():
    global oldest_access_time
    return oldest_access_time

class data:
    def __init__(self, object):
        self.object = object
    def getLastAccessTime(self):
        return dt.date.fromtimestamp(os.stat(self.object).st_atime)
    def setExpirationDate(self, days):
        self.expiration_date = self.getLastAccessTime() + dt.timedelta(days = days)
        setYoungestATime(self.getLastAccessTime())
        setOldestATime(self.getLastAccessTime())
    def isExpired(self):
        if dt.date.today() >= self.expiration_date:
            return True
        return False
for object in os.listdir(os.getcwd()):
    try:
        obj = data(object)
        obj.setExpirationDate(expiration)
        file_list.append(obj)
    except:
        print("There was an error with assigning "+object+" to obj")

cmake_dir(os.getcwd()+"\\"+str(getOldestATime())+" thru "+str(getYoungestATime())+"\\")

for files in file_list:
    if files.isExpired():
        shutil.move(os.getcwd()+"\\"+files.object, os.getcwd()+"\\"+str(getOldestATime())+" thru "+str(getYoungestATime())+"\\")
