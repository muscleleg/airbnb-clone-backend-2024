from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from .models import Room, Amenity
from rest_framework.views import APIView

from .serializers import AmenitySerializer


# Create your views here.
# def see_all_hello(request):
#     rooms = Room.objects.all()
#     return render(
#         request,
#         "all_rooms.html",
#         {"rooms": rooms, "title": "Hello! this title comes from django!"},
#     )
#
#
# def see_one_room(request, room_pk):
#     try:
#         room = Room.objects.get(pk=room_pk)
#         return render(request, "room_detail.html", {"room": room})
#     except Room.DoesNotExist:
#         return render(request, "room_detail.html", {"not_found": True})


class Amenities(APIView):
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(AmenitySerializer(amenity).data)
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(
            amenity, request.data, partial=True
        )  # partial=True를 꼭 줘야함, 일부만 업데이트 하겠다는것
        if serializer.is_valid():
            updated_amenity = (
                serializer.save()
            )  # 장고 모델 객체가 반환됨, 이를 json으로 변환해주기 위해 AmenitySerializer에 넣고 data를 뽑는거임
            return Response(AmenitySerializer(updated_amenity).data)  #
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk=pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)
