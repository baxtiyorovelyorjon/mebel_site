from django.contrib import admin

# Register your models here.
from blog.models import Mebel_turi, Brand, Mebel, OurBrand, Logo,Mebelforma

class MebelformaAdmin(admin.ModelAdmin):
    list_display = ['Ism','Tel','Manzil']
    list_filter = ['Ism']

admin.site.register(Mebel_turi)
admin.site.register(Brand)
admin.site.register(Mebel)
admin.site.register(OurBrand)
admin.site.register(Logo)
admin.site.register(Mebelforma)