from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'date_time_created', 'date_time_updated')  # فیلدهایی که در لیست ادمین نمایش داده می‌شن
    list_filter = ('status', 'author')  # فیلترهایی برای جستجو
    search_fields = ('title', 'text', 'author__username')  # جستجو بر اساس عنوان، متن و نام کاربری نویسنده
    date_hierarchy = 'date_time_created'  # مرتب‌سازی بر اساس تاریخ
    ordering = ('-date_time_created',)  # مرتب‌سازی پست‌ها از جدید به قدیم
    autocomplete_fields = ('author',)

admin.site.register(BlogPost, BlogPostAdmin)  # ثبت مدل در پنل ادمین
