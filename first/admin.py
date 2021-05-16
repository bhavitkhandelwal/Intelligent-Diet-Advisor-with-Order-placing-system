from django.contrib import admin
from .models import Contact,Product_gain,Product_loss

# Register your models here.
admin.site.register(Contact)
admin.site.register(Product_gain)
admin.site.register(Product_loss)