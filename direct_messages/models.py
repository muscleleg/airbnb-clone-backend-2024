from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):
    """Room Model Definition"""

    users = models.ManyToManyField(
        "users.User",
    )

    def __str__(self):
        return "Chatting Room"


class Message(CommonModel):
    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,  # 유저가 삭제되었다고 해서 메시지까지 삭제될건 없음, 선택임 근데 삭제 안할거임
    )  # 쪽지가 아님, 채팅방을 생각하면 이해가 됨, 채팅방에서는 보낸사람만 필요하기에 user하나면 됨
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,  # 채팅방이 삭제되면 메시지도 삭제되야함
    )

    def __str__(self):
        return f"{self.user} says: {self.text}"
