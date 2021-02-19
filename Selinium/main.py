from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

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

    

    

    driver.execute_script("document.getElementsByTagName('Button')[20].click()")

    slot_Times = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "booking-slot-item"))
    )

    info = [[],[]]

    for bookings in slot_Times :

        spots_avalible = bookings.find_element_by_tag_name("span")

        info[0].append(spots_avalible.text.split(" ", 1)[0])

    for bookings in slot_Times :

        spots_avalible = bookings.find_element_by_tag_name("strong")

        info[1].append(spots_avalible.text)

    for i in range(len(info[0])):
        print(info[0][i] + " " + info[1][i])



    

        


        
        
        

   



login()
time_slots()














