from django.contrib import admin
from .models import Category, Product, Cart, Women, Kid, WomenCart, KidsCart, EndSale, EndSaleCart

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']  
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'description', 'image', 'category']
    list_filter = ['category', 'product_price']  
admin.site.register(Product, ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']
    list_filter = ['user', 'product__category']  
admin.site.register(Cart, CartAdmin)

class WomenAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productprice', 'description', 'image', 'category']
    list_filter = ['category', 'productprice']  
admin.site.register(Women, WomenAdmin)

class WomenCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'women']
    list_filter = ['user', 'women__category'] 
admin.site.register(WomenCart, WomenCartAdmin)

class KidAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image', 'category']
    list_filter = ['category', 'price']  
admin.site.register(Kid, KidAdmin)

class KidCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'kid']
    list_filter = ['user', 'kid__category'] 
admin.site.register(KidsCart, KidCartAdmin)

class EndSaleAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'description', 'image', 'category']
    list_filter = ['category', 'product_price']  
admin.site.register(EndSale, EndSaleAdmin)

class EndSaleCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'endsale']
    list_filter = ['user', 'endsale__category']  
admin.site.register(EndSaleCart, EndSaleCartAdmin)
