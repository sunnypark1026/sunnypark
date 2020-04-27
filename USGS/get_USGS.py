"""
Last edited on Mon Apr 20 19:54:00 2020
@author: sunhee park
Scrapping the data from the US gov spending website Using selenium. 
"""

from selenium import webdriver # allow launching browser
# Opening in incognito
driver_option = webdriver.ChromeOptions()
#driver_option.add_argument(" — incognito")
chromedriver_path = 'C:/Users/sunhee/OneDrive/Documents/chromedriver/chromedriver' # Change this to your own chromedriver path!

# Creating a webdriver.
def create_webdriver():
 return webdriver.Chrome(executable_path=chromedriver_path, options=driver_option)


# Opening the website from the browser.
browser = create_webdriver()
browser.implicitly_wait(1)

# The different parts of the website splits
p1 = "https://www.usgovernmentspending.com/compare_state_spending_"
p2 = "1957"
p3 = "bH0a"

# URL concatenating the three different parts.
url = p1+p2+p3
# Getting the url.
browser.get(url)
# Clicking the button.
elem1 = browser.find_element_by_link_text("download file")
# Clicking the button.
elem1.click()

# Casting.
p2 = int(p2)

while(p2 < 2020):
    # Going to the next page.
    p2 = p2+1
    p2 = str(p2)
    url = p1+p2+p3
    # Opening up the page.
    browser.get(url)
    # finding the element
    elem1 = browser.find_element_by_link_text("download file")
    # Clicking
    elem1.click()
    # Casting back again.
    p2 = int(p2)

