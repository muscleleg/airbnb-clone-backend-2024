from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
    file = models.ImageField()
    description = models.CharField(
        max_length=140,
    )
    # room이랑 experience 둘다 사용될거임
    # manyToOne관계, 여러개의 사진은 하나의 룸에 속할 수 있음
    rooms = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )
    # manyToOne관계, 여러개의 사진은 하나의 experience에 속할 수 있음
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):
    file = models.FileField()
    # 일대일관계 비디오는 하나의 experience에 속하고 experience에는 하나의 video가 속함
    # 일대일관계는 결제정보를 저장할때도 주로 사용한다고 함
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Video File"
