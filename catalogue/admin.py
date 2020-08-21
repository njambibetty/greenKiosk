from django.contrib import admin

# Register your models here.
from .models import ProductSupplier, ProductCategory, Product, ProductImage, ProductReview

admin.site.register(ProductSupplier)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductReview)

