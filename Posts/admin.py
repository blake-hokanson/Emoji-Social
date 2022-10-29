from django.contrib import admin
from .models import Post, Message # Idk if these are correct names, adjust appropriately
admin.site.register(Post)
admin.site.register(Message)