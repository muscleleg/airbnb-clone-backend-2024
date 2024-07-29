from django.db import models
from common.models import CommonModel


class Booking(CommonModel):
    """Booking Model Definition"""

    class BookingKindChoices(models.TextChoices):
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    kind = models.CharField(
        max_length=15,
        choices=BookingKindChoices.choices,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # user가 지워지면 booking도 같이 지워짐
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,  # room이 지워지면 booking의 room에 null이 들어감
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    check_in = models.DateField(
        null=True,
        blank=True,
    )  # 날짜만 신경씀
    check_out = models.DateField(
        null=True,
        blank=True,
    )  # 날짜만 신경씀
    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )  # 날짜, 시간 신경씀
    guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.kind.title()} booking for: {self.user}"
