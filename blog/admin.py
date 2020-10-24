from django.contrib import admin

# Register your models heddre.
from .models import Post,Comment

admin.site.register(Post)
admin.site.register(Comment)
