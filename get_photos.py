from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementNotVisibleException
)
#import requests
import shutil
import os

def save_image_to_file(image, dirname, suffix):
    with open('{dirname}/img_{suffix}.jpg'.format(dirname=dirname, suffix=suffix), 'wb') as out_file:
        shutil.copyfileobj(image.raw, out_file)


def download_images(prefix, dirname, links):
    length = len(links)
    for index, link in enumerate(links):
        print('Downloading {0} of {1} images'.format(index + 1, length))
        url = prefix + link
        response = requests.get(url, stream=True)
        save_image_to_file(response, dirname, index)
        del response




def init_driver():
    driver = webdriver.Safari()
    driver.wait = WebDriverWait(driver, 1)
    return driver


def make_dir(dirname):
    current_path = os.getcwd()
    path = os.path.join(current_path, dirname)
    if not os.path.exists(path):
        os.makedirs(path)

def get_all_download_links(driver, url):
    '''Visits a page and retrieves all download links using regex'''
    driver.get(url)
    matches = re.findall(
        r'(?<=//s3.amazonaws.com).+.(?=uxga.jpg)', driver.page_source)

    matches = ["//s3.amazonaws.com" + s + "uxga.jpg" for s in matches]
    matches = list(map(lambda x: x.rsplit(' ', 1)[-1][2:], matches))
    matches = ["https://" + s for s in matches]

    return matches



import urllib.request
driver = init_driver()
matches = get_all_download_links(driver, "https://www.shoot.everphotoshoot.com/-/galleries/sazn1901050301")
driver.quit()

import socket
socket.gethostbyname("")

for index, link in enumerate(matches):
    urllib.request.urlretrieve(link, str(index) + ".jpg")




