from django.contrib import admin

from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    list_filter = ['customer', 'category']
    search_fields = ['title']
    exclude = ['IMAGE']
    ordering = ['price']

    def has_delete_permission(self, request, obj = ...):
        return False 
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj = ...):
        return False 

admin.site.register(Category)

