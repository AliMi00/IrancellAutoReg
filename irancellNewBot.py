from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class irancellBot():
    def __init__(self):
        #open chrome
        option = webdriver.ChromeOptions()
        option.add_argument('--ignore-certificate-errors')

        chromePath = 'G:\drive_D\Python\seleniumVenv\selenium-try\IrancellAutoReg\chromedriver.exe'

        self.driver = webdriver.Chrome(chromePath,chrome_options=option)

    #login 
    def login(self):
        self.driver.get("https://sale.irancell.ir")

        #defind element 
        user = self.driver.find_element_by_name('dealerusername')
        pas = self.driver.find_element_by_name('dealerpassword')
        pasOtp = self.driver.find_element_by_name('otp')

        otp = input('insert and enter the otp : ')
        username = input('Enter username :')
        password = input('enter pass word : ')

        #pass data
        pas.send_keys(password)
        user.send_keys(username)
        pasOtp.send_keys(otp)

        loginSub = self.driver.find_element_by_xpath('//*[@id="loginform"]/div[5]/div/div/button')
        loginSub.click()

        


        










        
