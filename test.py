from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

obj = None
def days_left():
    dateformat = "%Y-%m-%d %H:%M:%S"
    currentTime = datetime.strptime(str(datetime.now().strftime(dateformat)), dateformat)
    kjBday = datetime.strptime("2017-12-24 00:00:00", dateformat)

    diff = kjBday - currentTime

    if diff.total_seconds() < 0:
        obj.send_keys("Wish you Many Many Happy Returns of the Day Karishma !!! ")
        obj.send_keys(Keys.RETURN)
        print "DONE..."
        exit(0)
    days = diff.days
    hours = (diff.seconds)/3600
    minutes = (diff.seconds/60)%60
    seconds = diff.seconds%60

    if days==1:
        s_days="day"
    else:
        s_days="days"
    if hours==1:
        s_hours="hour"
    else:
        s_hours="hours"
    if minutes==1:
        s_minutes="minute"
    else:
        s_minutes="minutes"
    if seconds == 1:
        s_seconds="second"
    else:
        s_seconds="seconds"

    return str(days) + " "+ s_days +" " + str(hours) + " " + s_hours + " " + str(minutes) + " " + s_minutes +" " + str(seconds) + " " + s_seconds

def clickOnImage():
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/span/img').click()
            break
        except NoSuchElementException:
            print "element not found"
            pass

driver = webdriver.Chrome("C:\\Users\\vinay\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
print "WAITING..."
time.sleep(15)
print "GOING.."


clickOnImage()
while True:
    while True:
        counter=0
        while counter > 40:
            try:
                driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/div/header/div/div/button').click()
                counter=0
            except:
                pass
            clickOnImage()
        try:
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/div/div/div[4]/div[2]/div[2]/div[2]/span[1]/div/span').click()
            counter=0
            break
        except NoSuchElementException:
            counter = counter + 1
            print "element not fount 2"
            pass
        except:
            print "some error"
            pass

    
    while True:
        try:
            obj = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/div/div/div[4]/div[2]/div[2]/div[1]/div[2]')
            break
        except NoSuchElementException:
            print "element not found 3"
            pass
        except:
            print "some error"
            pass
            
    
    try:
        obj.clear()
        obj.send_keys(days_left())
        obj.send_keys(" to go... !!!")
        obj.send_keys(Keys.RETURN)
        print "Updated..."
        continue
    except:
        print "some error"
        pass


print "DONE>>>"
driver.close()
