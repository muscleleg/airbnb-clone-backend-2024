from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",  # str로도 컬럼을 사용할 수 있음
        "payload",
    )


# Register your models here.
