from django.db import models
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Blog_data(models.Model):
    text = models.CharField(max_length=200)
    link = models.URLField()

    def publish(self):
        self.save()

    #제목을 링크의 주소로
    def __str__(self):
        return self.text

class Market_data(models.Model):

    title = models.CharField(max_length=200) #글 제목
    writer = models.CharField(max_length=100) #작성자
    date = models.CharField(max_length=100) #작성 날짜
    text = models.TextField() #글 내용
    at_file_name1 = models.CharField(max_length=100, default='some')  #첨부파일 이름
    at_file_name2 = models.CharField(max_length=100, default='some')  # 첨부파일 이름
    at_file_name3 = models.CharField(max_length=100, default='some')  # 첨부파일 이름
    at_file_name4 = models.CharField(max_length=100, default='some')  # 첨부파일 이름

    download_link1 = models.CharField(max_length=200, default='some')  #첨부파일 html 링크
    download_link2 = models.CharField(max_length=200, default='some')  # 첨부파일 html 링크
    download_link3 = models.CharField(max_length=200, default='some')  # 첨부파일 html 링크
    download_link4 = models.CharField(max_length=200, default='some')  # 첨부파일 html 링크
    anchor = models.CharField(max_length=10, default='some')

    def __str__(self):
        return self.title



    