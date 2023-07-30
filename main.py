from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

TCB_USERNAME = ""
TCB_PASSWORD = ""

service = Service(r"C:\Users\Troxa\OneDrive\Рабочий стол\chromedriver.exe")
driver = webdriver.Chrome(service=service)

class LoginToTcb:
    def login_step1(self):
        driver.get("https://login.tcb.ac.il/nidp/saml2/sso?id=tcbloa2&sid=0&option=credential&sid=0")
        time.sleep(5)

        username = driver.find_element(By.ID,"Ecom_User_ID")
        username.send_keys(TCB_USERNAME)
        username.send_keys(Keys.ENTER)
        time.sleep(5)

    def login_step2(self):
        password = driver.find_element(By.ID,"ldapPasswordCardClick").click()
        time.sleep(5)

    def login_step3(self):
        time.sleep(5)
        password = driver.find_element(By.ID,"ldapPassword")
        password.send_keys(TCB_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)


class LinkedInJobs:
    def login_linkedIn(self):
        driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")
        time.sleep(5)
        username = driver.find_element(By.ID,'username')
        password = driver.find_element(By.ID,'password')

        username.send_keys("")
        password.send_keys("")
        password.send_keys(Keys.ENTER)

        time.sleep(10)

        driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3496291897&distance=25&geoId=101620260&keywords=DevOps%20Engineer&refresh=true")
        jobs = driver.find_elements(By.CSS_SELECTOR,"")


# tcb = LoginToTcb()
# tcb.login_step1()
# tcb.login_step2()
# tcb.login_step3()
linkedIn = LinkedInJobs()
linkedIn.login_linkedIn()
