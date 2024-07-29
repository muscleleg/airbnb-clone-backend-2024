from django.apps import AppConfig


class CategoriesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "categories"  # 모델은 category로 생성 후 meta를 통해 categories로 변경함
