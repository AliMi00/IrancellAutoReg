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

        


        

    def addToChart(self):
        self.driver.get('https://sale.irancell.ir/Product/5b28b561d0b9643bbc68fb46/Prepaid%20SP%20SIM')
        btnSim = self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div[1]/div[3]/div/div/div/div/div[2]/div/button')
        btnSim.click()

        #click cart
        cartElm = self.driver.find_element_by_xpath('//*[@id="wrapper"]/div/nav/div/ul[2]/li[2]/a/i')
        #cartElm.click()
        
        CartGo = self.driver.find_element_by_xpath('//*[@id="wrapper"]/div/nav/div/ul[2]/li[2]/ul/li[2]/div/a/div[3]/span')
        CartGo.click()

        simSerial = self.driver.find_element_by_xpath('//*[@id="kit_number0"]')
        simSerial.send_keys('')

        self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div[1]/div[3]/div/div/div/div/table/tbody/tr[1]/td[2]/div[1]/span/button').click()

        self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div[1]/div[3]/div/div/div/div/table/tbody/tr[1]/td[2]/div[2]/span/span/a').click()

        simMs = self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div[1]/div[3]/div/div/div/div/table/tbody/tr[1]/td[2]/div[2]/span/input')
        simMs.send_keys('')

        self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div[1]/div[3]/div/div/div/div/table/tbody/tr[1]/td[2]/div[2]/span/button').click()

        self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div[1]/div[3]/div/div/div/div/button[1]').click()

        # customer info 

        n_id = self.driver.find_element_by_name('nID')
        n_id.send_keys()
        
        first_name = self.driver.find_element_by_name('first_name')
        first_name.send_keys()

        last_name = self.driver.find_element_by_name('last_name')
        last_name.send_keys()

        brith_date = self.driver.find_element_by_xpath('//*[@id="undefined-1370-06-06--39074"]')
        brith_date.send_keys()

        father_name = self.driver.find_element_by_name('father_name')
        father_name.send_keys('')

        identity_code = self.driver.find_element_by_name('identity_code')
        identity_code.send_keys('0')

        gender = self.driver.find_element_by_xpath('//*[@id="select-gender"]')
        gender.click()

        man = self.driver.find_element_by_xpath('//*[@id="menu-gender"]/div[2]/ul/li[2]').click()
        female = self.driver.find_element_by_xpath('//*[@id="menu-gender"]/div[2]/ul/li[3]')

        email = self.driver.find_element_by_name('email')
        email.send_keys('a@a.com')

        mobile = self.driver.find_element_by_name('mobile')
        mobile.send_keys('')

        tel_code = self.driver.find_element_by_name('tel_code')
        tel_code.send_keys('')

        tel = self.driver.find_element_by_name('tel')
        tel.send_keys('')

        postal_code = self.driver.find_element_by_name('postal_code')
        postal_code.send_keys('')

        address = self.driver.find_element_by_name('address')
        address.send_keys('خ')

        building_number = self.driver.find_element_by_name('building_number')
        building_number.send_keys('0')



        









        
