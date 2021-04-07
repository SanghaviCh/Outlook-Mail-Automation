from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://outlook.live.com/owa/")


email = driver.find_element_by_xpath("//header/div[1]/aside[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]").click()

time.sleep(10)
ID = driver.find_element_by_xpath("//input[@id='i0116']")
ID.send_keys("leviackerman47@outlook.com")
driver.find_element_by_xpath("//input[@id='idSIButton9']").click()
time.sleep(10)

pwd = driver.find_element_by_xpath("//input[@id='i0118']")
pwd.send_keys("K@nna123")
driver.find_element_by_xpath("//input[@id='idSIButton9']").click()
time.sleep(10)

nm = driver.find_element_by_xpath("//span[@class='ms-Button-label sDjQm2-pu3zdQ7E2MIynW label-56']")
nm.click()
time.sleep(10)

to = driver.find_element_by_xpath("//input[@class='ms-BasePicker-input pickerInput_cf6f1afa']")
to.send_keys("Erenyeager961@outlook.com")
#time.sleep(15)

txt = driver.find_element_by_xpath("//div[@dir='ltr']")
txt.send_keys("hello")

sub = driver.find_element_by_xpath("//input[@placeholder='Add a subject']")
sub.send_keys("selenium automation test mail")

snd = driver.find_element_by_xpath("//div[@aria-label='Send']")
snd.click()

time.sleep(10)

driver.close()

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://outlook.live.com/owa/")
email = driver.find_element_by_xpath("//header/div[1]/aside[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]").click()

time.sleep(10)

ID = driver.find_element_by_xpath("//input[@id='i0116']")
ID.send_keys("Erenyeager961@outlook.com")
driver.find_element_by_xpath("//input[@id='idSIButton9']").click()
time.sleep(10)

pwd = driver.find_element_by_xpath("//input[@id='i0118']")
pwd.send_keys("K@nna123")
driver.find_element_by_xpath("//input[@id='idSIButton9']").click()
