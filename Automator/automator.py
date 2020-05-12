"""this should be able to automate a real repetitive task I use, for example, push a new google calendar event, open my school system including authentication"""

from selenium import webdriver
from time import sleep as sleep
import base64
base = str(base64.b64decode("sss"))
base = base[2:len(base)-1]


driver = webdriver.Chrome(executable_path=r'C:\Users\User\Desktop\Coding\Python\Automator\chromedriver_win32\chromedriver.exe')
driver.page_source.encode("UTF-8")

def log_into_gmail():
    user = "alexandrefreitas@cwbim.com.br"
    psw = base

    driver.get("https://gmail.com")
    username = driver.find_element_by_id("identifierId")
    username.send_keys(user)

    driver.find_element_by_class_name("CwaK9").click() #clicksnext

    sleep(2) #waits 2 secs so that page fully loads

    password = driver.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
    password.send_keys(psw)

    driver.find_element_by_xpath("//span [@class = 'RveJvd snByac']").click() #clicksnext

    sleep(5)
    #driver.close()


def harvest_fill():
    hours = 4
    week = [3, 4, 5, 6, 7]

    log_into_gmail()
    sleep(8)
    driver.get("https://id.getharvest.com/sessions/new")
    sleep(3)
    signgoogle = driver.find_element_by_xpath("/html/body/main/div[1]/a")
    signgoogle.click()
    sleep(3)
    thisweek_button = driver.find_element_by_xpath("//*[@id='weekly-timesheets-wrapper']/div/div/header/div[2]/div[1]/button[2]")
    thisweek_button.click()
    sleep(1)
    for days in week:
        fill = driver.find_element_by_xpath(
            "//*[@id='weekly-timesheets-wrapper']/div[1]/div/section/table[1]/tbody/tr[2]/td["+str(days)+"]/input")
        fill.send_keys(hours)


harvest_fill()
