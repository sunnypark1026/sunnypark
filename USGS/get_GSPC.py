"""
Created on Tue Apr 21 20:02:32 2020

@author: sunhee park

"""

# Importing all the necassary libraries
from selenium import webdriver # allow launching browser
# Opening in incognito
driver_option = webdriver.ChromeOptions()
driver_option.add_argument(" — incognito")
chromedriver_path = 'C:/Users/sunhee/OneDrive/Documents/chromedriver/chromedriver' # Change this to your own chromedriver path!

# Creating a webdriver.
def create_webdriver():
 return webdriver.Chrome(executable_path=chromedriver_path, options=driver_option)

# URLs
url = "https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC"
url2 = "https://query1.finance.yahoo.com/v7/finance/download/%5EGSPC?period1=1555984254&period2=1587606654&interval=1d&events=history"

# Opening the website from the browser.
browser = create_webdriver()

# Getting and downloading the data.
browser.get(url)
browser.implicitly_wait(3)
browser.get(url2)
