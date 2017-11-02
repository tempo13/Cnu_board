from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from blog.models import Blog_data

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def blog_data(request):
    parser_data = Blog_data.objects.filter(text__contains="[인재개발원]")
    return render(request, 'blog/post_list.html', {'parser':parser_data})

