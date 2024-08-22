from django.contrib import admin
from .models import Room, Amenity


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
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
