from django.contrib import admin
from .models import Album,Song

# include album module in admin
admin.site.register(Album)

# include song module in admin
admin.site.register(Song)

