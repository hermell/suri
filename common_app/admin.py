from django.contrib import admin
from common_app.models import Menu

class MenuAdmin(admin.ModelAdmin):
    # list_display = Menu._meta.get_all_field_names()
    list_display = ('id', 'name', 'level', 'kind', 'ordered', 'thumbnail', 'href_attr', 'register_date', 'register_id', 'update_date', 'update_id',)
    list_filter = ('id', 'name', 'level', 'kind', 'register_date', 'update_date',)

admin.site.register(Menu, MenuAdmin)