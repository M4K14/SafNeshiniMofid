from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

Username=str(input("Username? "))
Password=str(input("Password? "))
NameSahm=str(input("Esme Sahihe Sahm ro be Farsi benevis? "))
HowMany=int(input('ChandTa sahm mikhay?--> '))
Price=int(input('Be Che gheymati mikhay (Rials)?--> '))
StartingPoint=str(input("az key shorou beshe? (mesal-> 08:29:56)--> "))
duration=int(input('Baraye chand saniye hey order befreste??--> '))

def findsahm():
    Xpath=driver.find_element_by_xpath("/html/body/app-container/app-content/div/div/div/div[3]/div[1]/ul[1]/li[2]/div/symbol-search/div/angucomplete/div/input")
    Xpath.send_keys(str(NameSahm))
    time.sleep(1)
    Xpath.send_keys(Keys.DOWN)
    Xpath.send_keys(Keys.ENTER)

def sendorder():
    driver.find_element_by_id("send_order_txtCount").send_keys(str(HowMany))
    driver.find_element_by_id("send_order_txtPrice").send_keys(str(Price))
    driver.find_element_by_id("send_order_btnSendOrder").click()
    driver.find_element_by_id("send_order_txtCount").clear()
    driver.find_element_by_id("send_order_txtPrice").clear()

def orderloop():
    timer=driver.find_element_by_class_name("clock")
    if timer.text>=StartingPoint:
        t_end = time.time() + duration
        while time.time() < t_end:
            sendorder()
            time.sleep(0.5)
        else:
            print("--> Anjam Shoud <--")
            time.sleep(300)
            driver.quit()

driver= webdriver.Chrome()
driver.get('https://mofidonline.com/login')
driver.find_element_by_name('username').send_keys(Username)
driver.find_element_by_name('password').send_keys(Password)
captcha= driver.find_element_by_name('capcha')
driver.find_element_by_name('password').send_keys(Keys.TAB)
time.sleep(4)
captcha.send_keys(Keys.ENTER)
driver.fullscreen_window()
time.sleep(6)
findsahm()

def KeepSessionAlive():
    t_end0 = time.time() + 60*7
    while time.time() < t_end0:
        orderloop()
        time.sleep(0.1)
    else:
        driver.refresh()
        driver.fullscreen_window()
        time.sleep(3)
        findsahm()
        KeepSessionAlive()

KeepSessionAlive()

print("Done")