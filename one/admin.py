from django.contrib import admin
from . models import Publisher,Store,Book
# Register your models here.
admin.site.register(Publisher)
admin.site.register(Store)
admin.site.register(Book)