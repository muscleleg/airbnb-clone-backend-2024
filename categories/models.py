from django.db import models
from common.models import CommonModel


class Category(CommonModel):
    """Room or Experience Category"""

    class CategoryKindChoices(models.TextChoices):
        ROOMS = ("rooms", "Rooms")  # 값, 표시할 이름
        EXPERIENCES = (
            "experiences",
            "Experiences",
        )  # 기본적으로 튜플임을 표시하기 위해서 괄호를 붙여야 하지만 두개이상일때는 생략가능함, 한개일때는 써야함

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
