from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pytz
import time 


tz_NY = pytz.timezone('America/New_York') 
PATH = "/Users/samkettlewell-sites/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://urecregister.jmu.edu/booking/616cef9a-9c96-4ac8-8d12-9050261bfb85")




def login():

    try:
        
        login_user = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID, "txtUsername"))
        )

        login_pass = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID, "txtPassword"))
        )

        enter = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID, "btnLogin"))

    )
        p = open("pass.txt", "r")

        time.sleep(1)

        login_user.send_keys(p.readline())

        time.sleep(1)

        login_pass.send_keys(p.readline())

        time.sleep(1)

        p.close()

        enter.send_keys(Keys.RETURN)

    except:
        driver.quit()




def time_slots():

    time.sleep(5)


    try:

        driver.execute_script("document.getElementsByTagName('Button')[21].click()")

        time.sleep(10)

        driver.execute_script("document.getElementsByTagName('Button')[44].click()")

        print("compleated")
        driver.close()

    except:
        driver.close()




def pull_time():

    datetime_NY = datetime.now(tz_NY)

    
    print(datetime_NY.strftime("%H"))
    
    
    if "00" == datetime_NY.strftime("%H"):
        
        login()
        time_slots()
        time.sleep(81000)

    time.sleep(1200)
    
    pull_time()
    


pull_time()