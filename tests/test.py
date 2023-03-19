import seleasium
import selenium
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options

"""Testing stuff below before class definition"""
chrome_options = Options()
#keeps window open after execution
chrome_options.add_experimental_option("detach", True)

#create Selenium driver object that uses Chrome
driver = wd.Chrome(options=chrome_options)

#logging in to google drive
driver.get("https://accounts.google.com/signin/v2/identifier?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.maximize_window()
#sample input xpath -> /html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input

"""More testing stuff"""

sleezy = seleasium.seleasy(driver=driver)

sleezy.send_input("/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input", "taylor.r@intellese.com")
