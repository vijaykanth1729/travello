from django.contrib import admin
from .models import Product, Language, Framework, Movie, Character, Forum, DemoPic


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'updated', 'active','timestamp']
    list_filter = ['active', 'price']
    list_editable = ['active','price']
    ordering = ['-updated']
    search_fields = ['title']
    readonly_fields = ('timestamp',)
    prepopulated_fields = {'slug':('title',)}



admin.site.register(Product, ProductAdmin)
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Movie)
admin.site.register(Character)
admin.site.register(Forum)
admin.site.register(DemoPic)
