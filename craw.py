from bs4 import BeautifulSoup
from selenium import webdriver

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django

django.setup()

from blog.models import Blog_data

def craw():
    cont_list = {}
    phantomjs = '/Users/parkjongwho/Documents/phantomjs-2.1.1-macosx/bin/phantomjs'
    driver = webdriver.PhantomJS(phantomjs)
    url = 'http://plus.cnu.ac.kr/_prog/_board/?code=sub07_070801&site_dvs_cd=kr&menu_dvs_cd=070801'
    driver.get(url)
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, "html.parser")
    for cont in soup.select('td.title > a'):
        link = 'http://plus.cnu.ac.kr/_prog/_board' + cont['href'][1:]
        text = cont.get_text()
        cont_list[text] = link

    return cont_list

if __name__ == '__main__':
    blog_data_dict = craw()
    for i,j in blog_data_dict.items():
        Blog_data(text=i, link=j).save()