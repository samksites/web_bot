from selenium import webdriver
PATH = "/Users/samkettlewell-sites/Downloads/chromedriver"
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time as tf

driver = webdriver.Chrome(PATH)
driver.get("https://urecregister.jmu.edu/booking/616cef9a-9c96-4ac8-8d12-9050261bfb85")

tf.sleep(2)

login_user = driver.find_element_by_id("txtUsername")

login_pass = driver.find_element_by_id("txtPassword")

enter = driver.find_element_by_id("btnLogin")

login_user.send_keys("kettlesh")

tf.sleep(.5)

login_pass.send_keys("IhateRunning4824!")

tf.sleep(.5)

enter.send_keys(Keys.RETURN)

tf.sleep(2)



buttons = driver.find_element_by_class_name("container-flex-start-justified")


elementList = buttons.find_elements_by_tag_name("button")












