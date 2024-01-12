from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import schedule
def connection_hirodai(driver_path,emailID,pwd): 
    driver = webdriver.Edge(executable_path=driver_path)
    driver.get("https://portal.hinet.hiroshima-u.ac.jp/")
    driver.find_element(By.ID,"login").submit()
    time.sleep(10)

    #如果网页不要求登录
    if driver.find_element(By.CLASS_NAME, "table") is not None:
        driver.find_element(By.CLASS_NAME, "table").click()
        driver.find_element(By.ID, "login").submit()
    #需要登录的情况
    else:
        driver.find_element(By.ID, "i0116").send_keys(emailID)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(5)
        driver.find_element(By.ID, "i0118").send_keys(pwd)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(5)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(5)
        driver.find_element(By.ID, "login").submit()
    time.sleep(10)
    print("connection!")
    driver.quit()

driver_path = "msedgedriver" 
#input your email and pwd(optional)
emailID = "-u.ac.jp"
pwd = "PASSWORDS"
#Sets the time of execution
schedule.every().day.at("04:10").do(connection_hirodai,driver_path, emailID, pwd)
schedule.every().day.at("14:10").do(connection_hirodai,driver_path, emailID, pwd)
while True:
    schedule.run_pending()
    time.sleep(30)
