from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import csv
import os




class irancellBot():
    def __init__(self):
        #open chrome
        option = webdriver.ChromeOptions()
        option.add_argument('--ignore-certificate-errors')

        chromePath = 'G:\drive_D\Python\chromeDriver\chromedriver.exe'

        self.driver = webdriver.Chrome(chromePath,chrome_options=option)
        self.driver.get("https://crm.irancell.ir")
        
        self.pageLoad('//*[@id="loginTable1"]/div[3]/input')
        self.login()
        sleep(1)
        print('loaded 1 ------------------------------------->')


    #login 
    def login(self):
        # self.driver.get("https://crm.irancell.ir")

        #defind element 
        user = self.driver.find_element_by_name('username')
        pas = self.driver.find_element_by_name('password')

        username = input('Please Enter Username : ')
        password = input('Please Enter Password : ')


        #pass data
        pas.send_keys(password)
        user.send_keys(username)
        # pasOtp.send_keys(otp)

        loginSub = self.driver.find_element_by_xpath('//*[@id="loginTable1"]/div[3]/input')
        loginSub.click()

    def kitDetails(self,kits):
        
        #go to reg page 
        self.driver.get('http://crm.irancell.ir/clm-ui/#/customers/quick-register-kit/kit-details/')
        self.pageLoad('/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div[2]/form/ttui-decorator[3]/div/div[2]/div[1]/sf-decorator[1]/div/div/input')

        regss = self.driver.find_element_by_xpath('/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div[2]/form/ttui-decorator[3]/div/div[2]/div[1]/sf-decorator[1]/div/div/input')        
        regss.send_keys(kits[0])
        regss.send_keys(Keys.TAB)

        regkit = self.driver.find_element_by_xpath('/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div[2]/form/ttui-decorator[3]/div/div[2]/div[1]/sf-decorator[2]/div/div/input')
        regkit.send_keys(kits[1])

        sleep(1)
        nextBtn = '/html/body/div/div/div/div/ui-view/div[2]/div[2]/div[2]/div[2]/button'
        fnext = self.driver.find_element_by_xpath(nextBtn)

        for i in range(2):
            if(self.driver.current_url == 'http://crm.irancell.ir/clm-ui/#/customers/quick-register-kit/select-offering/'):
                break
            try:
                fnext.click()
                sleep(0.5)

            except:
                print('Error to go select ofering page')
            

        self.pageLoad(nextBtn)
        for i in range(2):
            sleep(1)
            if(self.driver.current_url == 'http://crm.irancell.ir/clm-ui/#/customers/quick-register-kit/select-offering/'):
                sleep(1)
                snext = self.driver.find_element_by_xpath(nextBtn)
                snext.click()
        
                            
    def pageLoad(self,xpath):

        timeout = 5
        try:
            element_present = EC.presence_of_element_located((By.XPATH, xpath))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print ("Timed out waiting for page to load")

    def CustomerProfile(self , profile):
        nIdXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div/form/ttui-decorator[7]/div/div[2]/div[2]/sf-decorator[1]/div/div/input'
        firstNameXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div/form/ttui-decorator[8]/div/div[2]/div[1]/sf-decorator[1]/div/div/input'
        lastNameXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div/form/ttui-decorator[8]/div/div[2]/div[2]/sf-decorator[1]/div/div/input'
        fatherNameXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div/form/ttui-decorator[8]/div/div[2]/div[1]/sf-decorator[2]/div/div/input'
        genderMaleXpath = 'body > div > div > div > div > ui-view > div.row.ng-scope.has-extended-footer > div.equal-col.ng-scope > div.col-md-8.section-main > ui-view > div > div > form > ttui-decorator:nth-child(8) > div > div.panel-body.forms-ttui.row > div:nth-child(2) > sf-decorator:nth-child(2) > div > div > div.ng-pristine.ng-untouched.ng-valid > label:nth-child(1) > span'
        genderFemaleXpath = 'body > div > div > div > div > ui-view > div.row.ng-scope.has-extended-footer > div.equal-col.ng-scope > div.col-md-8.section-main > ui-view > div > div > form > ttui-decorator:nth-child(8) > div > div.panel-body.forms-ttui.row > div:nth-child(2) > sf-decorator:nth-child(2) > div > div > div.ng-pristine.ng-untouched.ng-valid > label:nth-child(2) > span'
        emailXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div/form/ttui-decorator[8]/div/div[2]/div[1]/sf-decorator[5]/div/div/input'
        brithXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div/form/ttui-decorator[8]/div/div[2]/div[2]/sf-decorator[3]/div/div/input'
        telFirstXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div/form/ttui-decorator[8]/div/div[2]/div[1]/sf-decorator[8]/div/div[1]/div/sf-decorator[1]/div/div/input'
        telSecXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div/form/ttui-decorator[8]/div/div[2]/div[1]/sf-decorator[8]/div/div[1]/div/sf-decorator[2]/div/div/input'
        mobileXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div/form/ttui-decorator[8]/div/div[2]/div[1]/sf-decorator[11]/div/div/input'
        brithNumXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div/form/ttui-decorator[8]/div/div[2]/div[2]/sf-decorator[8]/div/div/input'
        postCodeXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div/form/ttui-decorator[9]/div/div[1]/div[2]/div/ol/li/sf-decorator/div/sf-decorator[2]/div/div/div[1]/sf-decorator[4]/div/div/input'
        steetXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div/form/ttui-decorator[9]/div/div[1]/div[2]/div/ol/li/sf-decorator/div/sf-decorator[2]/div/div/div[1]/sf-decorator[13]/div/div/input'
        buildingNumXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div/form/ttui-decorator[9]/div/div[1]/div[2]/div/ol/li/sf-decorator/div/sf-decorator[2]/div/div/div[1]/sf-decorator[14]/div/div/input'
        nextBtnXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[2]/div[2]/div[2]/button[1]'
        catXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div/form/ttui-decorator[8]/div/div[2]/div[2]/sf-decorator[7]/div/div/select'
        otpPassXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[1]/div[2]/ui-view/div/div/form/ttui-decorator[8]/div/div[2]/div[1]/sf-decorator[13]/div/div/select'


        info = profile

        self.pageLoad(nIdXpath)
        nId = self.driver.find_element_by_xpath(nIdXpath)
        nId.send_keys(info[0])
        nId.send_keys(Keys.TAB)

        #for load the n
        sleep(0.5)

        fistName = self.driver.find_element_by_xpath(firstNameXpath)
        fistName.send_keys(info[1])

        lastName = self.driver.find_element_by_xpath(lastNameXpath)
        lastName.send_keys(info[2])

        fatherName = self.driver.find_element_by_xpath(fatherNameXpath)
        fatherName.send_keys(info[3])

        otpPass = Select(self.driver.find_element_by_xpath(otpPassXpath))
        otpPass.select_by_index(1)

        email = self.driver.find_element_by_xpath(emailXpath)
        email.send_keys(info[5])        
        
        brith = self.driver.find_element_by_xpath(brithXpath)
        brith.send_keys(info[6])
        
        telFirst = self.driver.find_element_by_xpath(telFirstXpath)
        telFirst.send_keys(info[9][:3])
        
        telsec = self.driver.find_element_by_xpath(telSecXpath)
        telsec.send_keys(info[9][3:])
        
        mobile = self.driver.find_element_by_xpath(mobileXpath)
        mobile.send_keys(info[9])

        brithNum = self.driver.find_element_by_xpath(brithNumXpath)
        brithNum.send_keys('0')
        
        postCode = self.driver.find_element_by_xpath(postCodeXpath)
        postCode.send_keys(info[10])
        
        street = self.driver.find_element_by_xpath(steetXpath)
        street.send_keys(info[11])
        
        buildingNum = self.driver.find_element_by_xpath(buildingNumXpath)
        buildingNum.send_keys('0')

        cat = Select(self.driver.find_element_by_xpath(catXpath))
        cat.select_by_index(1)



        if info[4] == 'male':
            genderMale = self.driver.find_element_by_css_selector(genderMaleXpath)
            genderMale.click()
        elif info[4] == 'female':
            genderFemale = self.driver.find_element_by_css_selector(genderFemaleXpath)
            genderFemale.click()
        
        
        nextBtn = self.driver.find_element_by_xpath(nextBtnXpath)
        nextBtn.click()
        sleep(1)
        try:
            nextBtn.click()
        except:
            print('E')
        


    def checkAndSend(self):
        checkBoxSelector = '/html/body/div/div/div/div/ui-view/div[2]/div[2]/div[1]/ui-view/div/form/div/div/label/input'

        self.pageLoad(checkBoxSelector)

        checkBox = self.driver.find_element_by_xpath(checkBoxSelector)
        checkBox.click()

        nextBtn4Xpath = '/html/body/div/div/div/div/ui-view/div[2]/div[2]/div[2]/div[2]/button[1]'
        nextBtn4 = self.driver.find_element_by_xpath(nextBtn4Xpath)
        nextBtn4.click()

        accXpath = '/html/body/div[3]/div/div/div[3]/button[1]'
        self.pageLoad(accXpath)
        acc = self.driver.find_element_by_xpath(accXpath)
        acc.click()


    def cancelingRegester(self):
        #self.driver.get('http://crm.irancell.ir/clm-ui/#/customers/quick-register-kit/kit-details/')
        
        cancelBtnXpath = '/html/body/div/div/div/div/ui-view/div[2]/div[2]/div[2]/div[1]/span'
        cancelBtn = self.driver.find_element_by_xpath(cancelBtnXpath)
        cancelBtn.click()

        confermXpath = '/html/body/div[3]/div/div/div[3]/button[1]'
        confirmBtn = self.driver.find_element_by_xpath(confermXpath)
        confirmBtn.click()

    def completRegester(self):

#TODO : problem to locate the button 
        nextBtn = self.driver.find_element_by_xpath('/html/body/div/div/div/div/ui-view/div[2]/div[2]/div[2]/div[2]/button')
        nextBtn.click()

        confirmXpath = '/html/body/div[3]/div/div/div[3]/button[1]'
        self.pageLoad(confirmXpath)
        confirmBtn = self.driver.find_element_by_xpath(confirmXpath)
        confirmBtn.click()

        sleep(1)
        doneBtnXpath = '/html/body/div/div/div/div/ui-view/div/div[2]/div[2]/div[2]/button'
        self.pageLoad(doneBtnXpath)
        donBtn = self.driver.find_element_by_xpath(doneBtnXpath)
        donBtn.click()


    def oneReg(self,kits,info):
        sleep(1)
        s.kitDetails(kits)
        sleep(1)
        if (s.driver.current_url == 'http://crm.irancell.ir/clm-ui/#/customers/quick-register-kit/customer-profile/'):
            s.CustomerProfile(info)
            sleep(2)
            if(s.driver.current_url == 'http://crm.irancell.ir/clm-ui/#/customers/quick-register-kit/review/'):
                sleep(3)
                s.checkAndSend()
                if(s.driver.current_url == 'http://crm.irancell.ir/clm-ui/#/customers/quick-register-kit/upload-documents/'):
                    sleep(4)
                    s.completRegester()
                else:
                    s.cancelingRegester()
                    return False
            else:
                s.cancelingRegester()
                return False
        else:
            s.cancelingRegester()
            return False
        return True        


class rege():
    def __init__(self):
        super().__init__()

        
# s = irancellBot()

path = 'G:\\t2.csv'
info = []
kits = []
allData = []
file = open(path,'r',encoding='utf-8')
reader = csv.reader(file)
failed = ['status']


for row in reader:
    allData.append(row)
    if row[0] != 'kit':

        info = row[2:]
        kits = row[:2]
        print('not pass')
        try:
            s = irancellBot()
            results = s.oneReg(kits,info)
            if results == False:
                try:
                    s.cancelingRegester()
                except:
                    print('Warning')             
        except:
            print(False)



# a = 0
# for i in allData:
#     i[15] = failed[a]
#     a += 1

# file = open(path,'w',newline='',encoding='utf-8')
# writer = csv.writer(file)
# writer.writerows(allData)




