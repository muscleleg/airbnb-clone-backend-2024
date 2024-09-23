from django.urls import path
from . import views

urlpatterns = [
    path(
        "", views.CategoryViewSet.as_view({"get": "list", "post": "create"})
    ),  # as_view의 역할은 http요청을 get과 post를 구분지어서 처리함
    path(
        "<int:pk>",
        views.CategoryViewSet.as_view(
            {"get": "retrieve", "put": "partial_update", "delete": "destroy"}
        ),
    ),
]
