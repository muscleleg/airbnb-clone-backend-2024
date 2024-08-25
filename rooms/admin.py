from django.contrib import admin
from .models import Room, Amenity


# request를 통해 어떤 사람이 요청한지 알 수 있음, 이를 통해 권한이 있는 사람만 요청하게 할 수도 있음
# queryset은 어떤 요소를 선택한건지 알 수 있음
@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices,)
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )
    list_filter = (
        "country",
        "price",
        "pet_friendly",
        "kind",
        "amenities",
    )
    search_fields = (
        # "name",
        # "=price",
        "owner__username",
    )
    # 검색활성화, 와일드 카드도 사용가능,
    # 예) ^name: startwith, 앞에 문자가 같으면, 아무것도 안붙이면 기본값은 포함되었을때임
    # =는 정확히 같을때
    # 소유자의 이름으로도 검색 가능, owner__username

    # def total_amenities(self, room): # 두번째에 room을 넣는 것은 관리자 패널임
    #     return room.amenities.count()


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        # 읽기 전용 옵션, created_at과 같이 자동으로 데이터가 입력되는 것은 사용자가 수정할 수 없음
        # 또한 클릭하여 들어가면 화면에서 안나옴 readonly field를 넣어주면 나옴
        "created_at",
        "updated_at",
    )


# Register your models here.
