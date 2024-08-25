from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [("good", "Good"), ("great", "Great"), ("awesome", "Awesome")]

    def queryset(self, request, reviews):
        # dir로 뭐가 있는 지 알 수 있음 dir(request)
        word = self.value()  # url 값
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


class ReviewFilter(admin.SimpleListFilter):
    title = "is Review Positive?"
    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return [("bad", "Bad"), ("good", "Good")]

    def queryset(self, request, reviews):
        if self.value() == "bad":
            return reviews.filter(rating__lt=3)
        elif self.value() == "good":
            return reviews.filter(rating__gte=3)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",  # str로도 컬럼을 사용할 수 있음
        "payload",
    )
    # relation_ship 필터도 만들 수 있음
    # filter는 순차적으로 내려감 WordFilter -> rating -> user__is_host ... -> room__pet_friendly
    list_filter = (
        ReviewFilter,
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )


# Register your models here.
