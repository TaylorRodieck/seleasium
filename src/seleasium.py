import selenium

#"""Testing stuff below before class definition"""
# chrome_options = Options()
# #keeps window open after execution
# chrome_options.add_experimental_option("detach", True)

# #create Selenium driver object that uses Chrome
# driver = wd.Chrome(options=chrome_options)

# #logging in to google drive
# driver.get("https://accounts.google.com/signin/v2/identifier?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
# driver.maximize_window()
# #sample input xpath -> /html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input

class seleasy:
     def __init__(self, driver):
          self.driver = driver
          
     def check_exists_by_xpath(self, xpath):
          try:
               driver = self.driver
               driver.find_element(by=selenium.webdriver.common.by.By.XPATH, value = xpath)
          except selenium.common.exceptions.NoSuchElementException:
               return False
          except Exception as e:
               raise e
          return True

     def click_xpath(self, xpath, singleClick = False, doubleClick = False, rightClick = False):
          try:
               driver = self.driver
               pathExists = seleasy.check_exists_by_xpath(xpath)
               action = selenium.webdriver.ActionChains(driver)

               if pathExists and singleClick and (doubleClick == False and rightClick == False):
                    action.click(xpath).perform()
                    return
               elif pathExists and doubleClick and (singleClick == False and rightClick == False):
                    action.double_click(xpath).perform()
                    return
               elif pathExists and rightClick and (singleClick == False and doubleClick == False):
                    action.context_click(xpath).perform()
                    return
               elif pathExists != True:
                    raise Exception("Path does not exist! ...  ):")
               else:
                    raise Exception("Check arguments! More than one 'click' option was set to true.")
          except Exception as e:
               raise e

     def get_accessible_name(self, xpath):
          try:
               driver = self.driver
               pathExists = seleasy.check_exists_by_xpath(xpath)
               if pathExists:
                    return str(driver.find_element(by=selenium.webdriver.common.by.By.XPATH, value=xpath).accessible_name)
               else:
                    raise Exception(xpath + " <- Element does not exist! ...  ):")
          except Exception as e:
               raise e

     def send_keys(self, keysToSend):
          try:
               driver = self.driver
               action = selenium.webdriver.ActionChains(driver)
               action.send_keys(keysToSend).perform()
               return
          except Exception as e:
               raise e

     def send_input(self, xpath, input_to_send):
          try:
               driver = self.driver
               driver.find_element(by=selenium.webdriver.common.by.By.XPATH, value = xpath).send_keys(input_to_send)
               return
          except Exception as e:
               raise e

#"""More testing stuff"""

#sleezy = seleasy(driver=driver)

#sleezy.send_input("/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input", "taylor.r@intellese.com")
