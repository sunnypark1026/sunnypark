""" 
Last edited on Sunday Apr 19 17:30:41 2020

@author: sunhee park 

Script description: Designed to download,modify and uploud the 
"""

# Importing all the necassary libraries
from selenium import webdriver # allow launching browser
import re
import pandas as pd

# Opening in incognito
driver_option = webdriver.ChromeOptions()
driver_option.add_argument(" — incognito")
chromedriver_path = 'C:/Users/sunhee/OneDrive/Documents/chromedriver/chromedriver' # Change this to your own chromedriver path!

# Creating a webdriver.
def create_webdriver():
 return webdriver.Chrome(executable_path=chromedriver_path, options=driver_option)

# URLs
url = "https://fred.stlouisfed.org/series/GDP#0"
url2 = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=GDP&scale=left&cosd=1947-01-01&coed=2019-10-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=avg&fgst=lin&fgsnd=2009-06-01&line_index=1&transformation=lin&vintage_date=2020-04-19&revision_date=2020-04-19&nd=1947-01-01"

# Opening the website from the browser.
browser = create_webdriver()

# Getting and downloading the data.
browser.get(url)
browser.get(url2)
