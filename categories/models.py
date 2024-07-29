from django.db import models
from common.models import CommonModel


class Category(CommonModel):
    """Room or Experience Category"""

    class CategoryKindChoices(models.TextChoices):
        ROOMS = ("room", "Room")
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(max_length=50)
    kind = models.CharField(
        max_length=15,
        choices=CategoryKindChoices.choices,
    )

    def __str__(self) -> str:
        return f"{self.kind.title()}: {self.name}"  # toString에서 rooms: Tiny Home과 같이 나옴, .tite() 맨 앞 문자를 대문자로 바꿈

    class Meta:
        verbose_name_plural = "Categories"
        # 모델 Category를 Cateories로 나오게함


# Create your models here.
