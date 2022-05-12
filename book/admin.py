from django.contrib import admin

# Register your models here.
# app01/admin.py:
from book.models import *


class BookAdmin(admin.ModelAdmin):
    list_per_page = 20
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True
    list_display = ['ISBN', 'BookTitle', 'BookAuthor', 'YearOfPublication', 'Publisher']


class UserAdmin(admin.ModelAdmin):
    list_per_page = 20
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True
    list_display = ['UserID', 'password', 'Location', 'Age']


class BookRatingsAdmin(admin.ModelAdmin):
    list_per_page = 20
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True
    list_display = ['ID', 'UserID', 'ISBN', 'BookRating']


# 注册Model类
admin.site.register(book, BookAdmin)
admin.site.register(user, UserAdmin)
admin.site.register(bookRatings, BookRatingsAdmin)