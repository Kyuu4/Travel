from django.contrib import admin
from .models import Customer, Category, Course

# Register your models here.
#admin.site.register(Customer)
#admin.site.register(Category)
#admin.site.register(Age)
#admin.site.register(Course)
#admin.site.register(Price)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ...

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("category", "name", 'kid_age', 'price', 'date_price', 'image')
    list_filter = ("category", "name")

