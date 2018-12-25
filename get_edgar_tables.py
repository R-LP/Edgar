#from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
import pandas as pd


driver = Firefox(options=opts)
driver.get('https://www.sec.gov/cgi-bin/viewer?action=view&cik=1341439&accession_number=0001193125-18-201034&xbrl_type=v')
driver.find_elements_by_link_text("Financial Statements")[0].click()
driver.find_elements_by_link_text("CONSOLIDATED BALANCE SHEETS")[0].click()

dfs = pd.read_html(driver.page_source, header=0)

# driver.find_elements_by_link_text("CONSOLIDATED STATEMENTS OF OPERATIONS")[0].click()
# dfs = pd.read_html(driver.page_source, header=0)

