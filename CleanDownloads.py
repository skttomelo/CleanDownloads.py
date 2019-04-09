import os, shutil
import datetime as dt

oldest_access_time = dt.date.today() # setting the oldest access time to today makes it possible to change oldest date
youngest_access_time = dt.date(1,1,1) # setting the the youngest date to the oldest date possible makes it possible to change the youngest date
expiration = 30 # number of days till something expires
file_list = []
downloads = "F:\\Downloads\\" # directory for the downloads folder
os.chdir(downloads) # current working directory is changed to the downloads folder

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

# this class stores the data of a file inside it
class data:
    def __init__(self, object):
        self.object = object
    def getLastAccessTime(self): # returns the last access time as a date (year-month-day)
        return dt.date.fromtimestamp(os.stat(self.object).st_atime)
    def setExpirationDate(self, days): # sets the date for when the file will be considered "unused"
        self.expiration_date = self.getLastAccessTime() + dt.timedelta(days = days)
        setYoungestATime(self.getLastAccessTime())
        setOldestATime(self.getLastAccessTime())
    def isExpired(self): # checks if the file is "unused"
        if dt.date.today() >= self.expiration_date:
            return True
        return False
for object in os.listdir(os.getcwd()):
    try: # We want to try to assign the object found in the directory to a data object, set its expiration, then append it to the list
        obj = data(object)
        obj.setExpirationDate(expiration)
        file_list.append(obj)
    except: # Not a good exception, but it is good for this test
        print("There was an error with assigning "+object+" to obj")

cmake_dir(os.getcwd()+"\\"+str(getOldestATime())+" thru "+str(getYoungestATime())+"\\")

for files in file_list: # we check if the files in file_list are expired, and if so then we move them to their designated expired location
    if files.isExpired():
        shutil.move(os.getcwd()+"\\"+files.object, os.getcwd()+"\\"+str(getOldestATime())+" thru "+str(getYoungestATime())+"\\")
