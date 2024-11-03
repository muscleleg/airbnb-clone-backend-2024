from django.utils import timezone
from rest_framework import serializers
from .models import Booking


class CreateRoomBookingSerializer(serializers.ModelSerializer):
    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
        )

    # validate_필드명을 하면 serializer.is_valid()할때 valdiate를 해줌
    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    # 모든 데이터 validate
    def validate(self, data):
        if data["check_out"] <= data["check_in"]:
            raise serializers.ValidationError(
                "Check in should be smaller than check out."
            )
        # 이부분이 중요함, in은 왼쪽 끝이고 out은 오른쪽 끝임
        # 비교대상이 되는 날짜의 끝인 out을 기준으로 왼쪽방향에 데이터가 있는 지 확인 해야함. 비교대상의 out은 데이터의 최대값임
        # 최대 값기준으로 그 아래에 데이터가 있는지 확인하는 것임, 기존 데이터의 최하위는 왼쪽끝(check_in)임. 비교 대상의 최대값을 기준으로 기준값 최소값이 있는지 확인하는것임
        # 반대로 비교값의 최소 값은 왼쪽끝 (check_in)임 왼쪽 끝값 기준으로 오른쪽에 값이 있는 지 확인 하는 것임
        # 이 둘에 모두 속한다면 그 날짜에는 데이터가 예약이 된 것이고 없다면 빈 날짜인 것임
        # < - - - - o 6일보다 작은 날짜에 check_in 있니?
        #     B B B
        #   I - - - > 2일보다 큰 날짜에 check_out 있니?
        # 1 2 3 4 5 6 7 8 9
        if Booking.objects.filter(
            check_in__lte=data["check_out"],
            check_out__gte=data["check_in"],
        ).exists():
            raise serializers.ValidationError(
                "Those (or some) of those dates are already taken."
            )
        return data


# 해당 표를 보고 생각하면 편함 2일(check_in)보다 높은 값의 check_out을 가진며 4일 보다 낮은 작은 check_in을 가진 booing
#    1 2 3 4 5 6 7 8 9


#      2 3 4
class PublicBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
        )
