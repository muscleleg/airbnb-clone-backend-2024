from django.contrib import admin
from .models import Category


@admin.register(Category)  # admin 파일을 안써주면 관리자페이지에 안나옴
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "kind",
    )
    list_filter = ("kind",)
