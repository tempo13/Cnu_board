from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from blog.models import Market_data



def parser(text, text_path):
    f = open(text_path, 'r+', encoding="UTF8")
    before=f.readline()
    latests = text
    if before != latests:
        f = open(text_path, 'w+', encoding="UTF8")
        f.write(latests)
        f.close()
        return True
    else:
        f.close()
        return False


def src_parser(url):
    phantomjs = os.path.expanduser("~")+'/Documents/phantomjs-2.1.1-macosx/bin/phantomjs'
    driver = webdriver.PhantomJS(phantomjs)
    driver.get(url)
    cont_info = requests.get(url)
    cont_info_cont = cont_info.content
    soup = BeautifulSoup(cont_info_cont, 'lxml')
    post_title = soup.select('div.board_viewTit > h4')
    post_writer = soup.select("ul.board_viewInfo > li.writer")
    post_date = soup.select("ul.board_viewInfo > li.date")
    post_cont = driver.find_element_by_xpath('//*[@id="txt"]/div[3]')
    content_text = post_cont.text  # 글 내용
    content_title = post_title[0].get_text()  # 제목
    content_writer = post_writer[0].get_text()[3:]  # 작성자
    content_date = post_date[0].get_text()[3:]  # 작성일
    #첨부파일 검사 후 파일 분류
    try:
        if driver.find_element_by_xpath("//*[@id='txt']/ul/li[4]/div/a[1]"):
            #장터는 a[1]부터 시작 게시판은 a[0]부터 시작
            for i in range(1,4):

                at_file=driver.find_element_by_xpath("//*[@id='txt']/ul/li[4]/div/a["+str(i)+"]")
                if at_file.text:
                    if at_file.text[-3:] == "pdf" or at_file.text[-3:] == "hwp":
                        #파일 확장자 검색 후 링크 넘겨 줌
                        at_file_down = driver.find_element_by_link_text(at_file.text).get_attribute('href')
                        Market_data(title=content_title,writer=content_writer,date=content_date,text=content_text,
                                    at_file_name=at_file.text ,download_link=at_file_down, anchor="doc").save()
                    if at_file.text[-3:] == "jpg" or at_file.text[-3:] == "png":
                        at_file_down = driver.find_element_by_link_text(at_file.text).get_attribute('href')
                        Market_data(title=content_title, writer=content_writer, date=content_date, text=content_text,
                                    at_file_name = at_file.text, download_link=at_file_down, anchor="img").save()
        else:
            Market_data(title=content_title, writer=content_writer, date=content_date, text=content_text,
                        anchor="docn").save()
    except:
        print("글이 없습니다")