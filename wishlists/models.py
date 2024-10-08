from django.db import models
from common.models import CommonModel


class Wishlist(CommonModel):
    """Wishlist Model Definition"""

    name = models.CharField(
        max_length=150,
    )
    rooms = models.ManyToManyField(  # 그냥 좋아요가 아니라 플레이리스트같은 리스트라 many to many가 가능함
        "rooms.Room",
        related_name="wishlists",
    )
    experiences = models.ManyToManyField(
        "experiences.Experience",
        related_name="wishlists",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="wishlists",
    )

    def __str__(self):
        return self.name


# Create your models here.
