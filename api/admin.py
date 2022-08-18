from django.contrib import admin
from .models import *

admin.site.register(Tree)
admin.site.register(TreeType)
admin.site.register(TreeName)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(TreePrice)
admin.site.register(Dashboard)
admin.site.register(Feedback)

class TreeInline(admin.TabularInline):
    model = Tree
    extra = 0
    verbose_name = 'Daraxt'
    verbose_name_plural = 'Daraxtlar'

class ClientAdmin(admin.ModelAdmin):
    inlines = [TreeInline]

admin.site.register(Client,ClientAdmin)
