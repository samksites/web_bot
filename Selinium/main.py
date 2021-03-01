from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import datetime
import psycopg2
# path varriable to the chrome driver
PATH = "/Users/samkettlewell-sites/Downloads/chromedriver"
# creates driver from the path varriable
driver = webdriver.Chrome(PATH)




class Main_find():
    # list of days ofthe week
    week_days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    # method is used to loginto urec page
    def login(self):
        # trys to log in if not returns back to accesses method
        try:
            # gets the url of urec login page
            driver.get("https://urecregister.jmu.edu/booking/616cef9a-9c96-4ac8-8d12-9050261bfb85")
            
            # Following steps locate the username, password and enter parts of the login page
            # will wait 10 seconds at max to find theses elements
            # all our found through their HTML ID
            login_user = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.ID, "txtUsername"))
            )

            login_pass = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.ID, "txtPassword"))
            )

            enter = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.ID, "btnLogin"))

        )
            # opens my password file
            # requires you to have a password txt file to run this program
            p = open("pass.txt", "r")

            # reads firs line of password file and sends my username
            login_user.send_keys(p.readline())

            #waits one second
            time.sleep(1)

            # acesss my password for the page
            login_pass.send_keys(p.readline())

            time.sleep(1)

            # closses password file
            p.close()

            # sends enter key message
            enter.send_keys(Keys.RETURN)

            
        # if anything fails quits the driver
        except:
            driver.quit()


    def time_slots(self, button_number):

        time.sleep(1)

        button_string ="document.getElementsByTagName('Button')[" + str(button_number) + "].click()"

        driver.execute_script(button_string)

        slot_Times = WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "booking-slot-item"))
        )
        info = [[],[]]

        times_avalible = []

        for bookings in slot_Times:

            spots_avalible = bookings.find_element_by_tag_name("span")

            info[0].append(spots_avalible.text.split(" ")[0])


            spots_avalible = bookings.find_element_by_tag_name("strong")

            times_avalible.append(spots_avalible.text)

        info[1] = self.cleanString(times_avalible)
            

        return info

    # funtion to clean data of time slots
    def cleanString(self, temp_data):

        time_slots = []

        # loops through all temporary data of when the time slots are
        for x in range(len(temp_data)):
            
            # removes all : from time ex 12:30 -- 1230
            hold = temp_data[x].replace(":", "")
           
            # figures out if data is is from the morning or evening and uses that info
            # to conver to millitary time
            if "PM" in hold and "12" not in hold and not "AM" in hold:
                # removes all info after the time
                hold = hold.split(" ")[0]
                # converts to a intager
                hold = int(hold)
                # checks value is less then 15 and mutiplies by 100
                if hold < 15:
                    hold *= 100
                # adds 1200 to be in the afternoon
                hold += 1200
            # else just multiplys by 100 and converts to integer
            else:
                hold = hold.split(" ")[0]
                hold = int(hold)
                if hold < 15:
                    hold *= 100

            # used to set time slots values on a half hour baseses so changes
            # ex: 1230 now equals 1250
            if hold % 100 == 30:
                hold += 20
            
            time_slots.append(hold)

        return time_slots


    

    def askForData(self):

        conn = psycopg2.connect(user="postgres",
                                  password="ihaterunning4824",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="Emerging")
        cur = conn.cursor()

        

        date_varrible = datetime.datetime.today().weekday()

        i = 0
        button = 19
        script = "INSERT INTO urec_data (day, reservationtime, spots, timetill) VALUES(%s,%s,%s,%s);"

        t = time.localtime()

        current_time = time.strftime("%H", t)

        current_time = (int(current_time) * 100)

        while i < 3:

            day = self.week_days[(date_varrible + i) % 7]
            info = self.time_slots(button + i)
            tempTipe = 24 * i * 10
            i += 1
            
            for x in range(len(info[0])):
                try:
                    spots = int(info[0][x])
                except:
                   
                    spots = (int(info[0][x - 1]) + int(info[0][x + 1])) / 2

                values = (day,info[1][x],spots, tempTipe + info[1][x] - current_time)

                cur.execute(script, values)
                conn.commit()

        cur.close()
        conn.close()

            
    def stay_still(self):
        time.sleep(3600)
        self.accesses()
        
        

    def accesses(self):
        self.login()
        self.askForData()
        self.accesses()
        
        

Main_find().accesses()






















