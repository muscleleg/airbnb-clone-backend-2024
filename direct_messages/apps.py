from django.apps import AppConfig


class DirectMessagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "direct_messages"
    verbose_name = "Direct Messages"  # 장고 어디민 패털에 표시되는 Direct_Message를 Direct Message로 바꿈
