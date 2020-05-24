from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class irancellBot():
    def __init__(self):
        #open chrome
        self.driver = webdriver.Chrome()

    #login 
    def login(self):
        self.driver.get("https://sale.irancell.ir")

        #defind element 
        user = self.driver.find_element_by_name('dealerusername')
        pas = self.driver.find_element_by_name('dealerpassword')
        pasOtp = self.driver.find_element_by_name('otp')

        otp = input('insert and enter the otp : ')

        #pass data
        pas.send_keys('_e41_e41')
        user.send_keys('ehsan.mob')
        pasOtp.send_keys(otp)

        loginSub = self.driver.find_element_by_xpath('//*[@id="loginform"]/div[5]/div/div/button')
        loginSub.click()

        


        










        
