from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Admin)
admin.site.register(Artist)
admin.site.register(ArtGalleryManager)
admin.site.register(Customer)
admin.site.register(Event)
admin.site.register(Product)
admin.site.register(Order)
