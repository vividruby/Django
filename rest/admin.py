from django.contrib import admin
from .models import Restaurant, Menu, Food

class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ['location']

admin.site.register(Menu)
admin.site.register(Food)
admin.site.register(Restaurant, RestaurantAdmin)