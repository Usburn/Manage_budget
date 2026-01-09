from django.contrib import admin

# Register your models here.
from .models import Depenses , AutresDepenses, Revenue


class DepenseAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)

class AutresDepensesAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
   
   


class RevenuAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
   



admin.site.register(Depenses,DepenseAdmin)
admin.site.register(AutresDepenses, AutresDepensesAdmin)
admin.site.register(Revenue, RevenuAdmin)

