from django.contrib import admin
from .models import Post
from .models import Blog_data
from .models import Market_data

admin.site.register(Post)
admin.site.register(Blog_data)
admin.site.register(Market_data)
# Register your models here.
